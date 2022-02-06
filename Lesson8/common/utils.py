"""Утилиты"""

import sys
import json
from Lesson8.common.variables import MAX_PACKAGE_LENGTH, ENCODING
from Lesson8.errors import IncorrectDataRecivedError, NonDictInputError
from Lesson8.decos import log


@log
def get_message(client):
    """
    Утилита приёма и декодирования сообщения принимает байты и выдаёт словарь,
    если принято что-то другое, отдаёт ошибку значения
    :param client:
    :return:
    """
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        else:
            raise IncorrectDataRecivedError
    else:
        raise IncorrectDataRecivedError


@log
def send_message(sock, message):
    """
    Утилита кодирования и отправки сообщения
    принимает словарь и отправляет его
    :param sock:
    :param message:
    :return:
    """
    if not isinstance(message, dict):
        raise NonDictInputError
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)