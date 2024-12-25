import os
from datetime import datetime
from time import sleep

from requests import request as http_request
from requests.exceptions import ConnectionError

from constants import APIResources, ExportFormat, DateDimension
from exceptions import AppmetricaClientError, AppmetricaApiError
from schemas.resource_schema_mapping import RESOURCES_SCHEMA_MAPPING


def send_request(url, params, headers, stream, request_latency, only_new_request):
    while True:
        try:
            response = http_request('GET', url=url, params=params, headers=headers, stream=stream)
            response.encoding = 'utf-8'

            code = response.status_code
            print(f'HTTP Status Code: {code}')

            if code == 200:
                print('Данные успешно получены.')
                print('----------------------------------\n')
                return response
            elif code in (201, 202):

                # После первого запроса в следующих запросах передавать заголовок Cache-Control не нужно
                if only_new_request:
                    only_new_request = False
                    headers.pop('Cache-Control')

                print(response.text)
                print(f'Повторный запрос через {request_latency} секунд')
                sleep(request_latency)
            else:
                raise AppmetricaApiError()

            print('----------------------------------\n')
        except ConnectionError:
            raise AppmetricaClientError(ConnectionError)


def get_metrics(application_id: str, oauth_token: str, export_format: str, resource: str, date_dimension: str,
                date_from: datetime, date_to: datetime, request_latency: int, only_new_request: bool, stream: bool,
                fields: list[str] = None):
    api_url = '/'.join(['https://api.appmetrica.yandex.ru/logs/v1/export', f'{resource}']) + f'.{export_format}'

    if resource in RESOURCES_SCHEMA_MAPPING.keys():
        fields = ','.join(
            list(RESOURCES_SCHEMA_MAPPING[resource].model_fields.keys())) if fields is None else ','.join(fields)
    else:
        raise AppmetricaClientError(f'Ресурс {resource} не доступен для экспорта.')

    params = {
        'application_id': application_id,
        'fields': fields,
        'date_dimension': date_dimension,
        'use_utf8_bom': 'true'
    }

    headers = {
        'Authorization': f'OAuth {oauth_token}'
    }

    # Если требуется получить новые данные, то добавляется заголовок Cache-Control: no-cache
    if only_new_request:
        headers.update({
            'Cache-Control': 'no-cache'
        })

    # Для всех ресурсов, кроме profiles и push_tokens надо указать диапазон дат.
    if resource not in (APIResources.PROFILES, APIResources.PUSH_TOKENS):
        if all([date_from, date_to]):
            dt_format = '%Y-%m-%d %H:%M:%S'
            params.update({
                'date_since': date_from.strftime(dt_format),
                'date_until': date_to.strftime(dt_format)
            })
        else:
            raise AppmetricaClientError(
                f'Для ресурса {resource} требуется указать диапазон дат - параметры date_from и date_to')

    print("URL: ", api_url)
    print("Params: ", params)
    print("Headers: ", headers)
    print("----------------------------------\n")

    response = send_request(api_url, params, headers, stream, request_latency, only_new_request)

    if stream is True:
        # Размер одного чанка в байтах, по умолчанию 10MB
        chunk_size = 10 * 1024 * 1024
        decode_unicode = False
        return response.iter_content(chunk_size=chunk_size, decode_unicode=decode_unicode)
    else:
        return response.content


def write_to_file(content, file_name, file_type, stream):
    with open(f'{file_name}.' + f'{file_type}', 'wb') as file:
        print(f'Запись в файл {file_name}.{file_type}')
        if stream:
            for chunk in content:
                print(f'Размер чанка: {len(chunk)} bytes')
                file.write(chunk)
        else:
            print(f'Размер документа: {len(content)} bytes')
            file.write(content)
        print('----------------------------------\n')
        print(f'Итоговый размер файла: {file.tell()} bytes')


if __name__ == '__main__':
    application_id = os.getenv('APPLICATION_ID', 'default_application_id')
    oauth_token = os.getenv('OAUTH_TOKEN', 'default_oauth_token')
    export_format = ExportFormat.CSV
    resource = APIResources.EVENTS
    date_dimension = DateDimension.DEFAULT
    date_from = datetime(2024, 12, 14, 0, 0, 0)
    date_to = datetime(2024, 12, 20, 23, 59, 59)
    request_latency = 10
    only_new_request = True
    stream = False

    file_name = "output"

    data_bytes = get_metrics(
        application_id,
        oauth_token,
        export_format,
        resource,
        date_dimension,
        date_from,
        date_to,
        request_latency,
        only_new_request,
        stream,
    )

    write_to_file(data_bytes, file_name, export_format, stream)
