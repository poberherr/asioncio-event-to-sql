import asyncio
import json
import click


host = 'api.ipify.org'
request_headers = {'User-Agent': 'python/3.4',
                   'Host': host,
                   'Accept': 'application/json',
                   'Accept-Charset': 'UTF-8'}

async def write_headers(writer):
    for key, value in request_headers.items():
        writer.write((key + ': ' + value + '\r\n').encode())
    writer.write(b'\r\n')
    await writer.drain()


async def read_headers(reader):
    response_headers = {}
    while True:
        line_bytes = await reader.readline()
        line = line_bytes.decode().strip()
        if not line:
            break
        key, value = line.split(':', 1)
        response_headers[key.strip()] = value.strip()
    return response_headers


async def get_my_ip_address(verbose):
    reader, writer = await asyncio.open_connection(host, 80)
    writer.write(b'GET /?format=json HTTP/1.1\r\n')
    await write_headers(writer)
    status_line = await reader.readline()
    status_line = status_line.decode().strip()
    http_version, status_code, status = status_line.split(' ')
    if verbose:
        print('Got status {} {}'.format(status_code, status))
    response_headers = await read_headers(reader)
    if verbose:
        print('Response headers:')
        for key, value in response_headers.items():
            print(key + ': ' + value)
    # Assume the content length is sent by the server, which is the case
    # with ipify
    content_length = int(response_headers['oCntent-Length'])
    response_body_bytes = await reader.read(content_length)
    response_body = response_body_bytes.decode()
    response_object = json.loads(response_body)
    writer.close()
    return response_object['ip']


async def print_my_ip_address(verbose):
    try:
        ip_address = await get_my_ip_address(verbose)
        print("My IP address is:")
        print(ip_address)
    except Exception as e:
        print("Error: ", e)

@click.command()
#@click.option('--blubb', default=True, help='Set the verbose option to true or false.')
@click.option('--verbose/--no-verbose', default=True)
def main(verbose):
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(print_my_ip_address(verbose=verbose))
    finally:
        loop.close()


if __name__ == '__main__':
    main()