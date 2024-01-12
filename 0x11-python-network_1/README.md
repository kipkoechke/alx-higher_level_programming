![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

> Python Networking #1

## About

This project involved learning how to use the `urllib` and `requests` Python
libraries to send and receive HTTP messages to URL's. I practiced sending `GET`
and `POST` requests, fetching JSON resources, and interacting with API's (the
Star Wars API, GitHub API, and Twitter API).

## Resources

**Read or watch**:

1. [How to fetch internet resources using the urrlib library](https://docs.python.org/3/howto/urllib2.html)
2. [Quickstart with the requests package](https://requests.readthedocs.io/en/latest/)
3. [Requests package](https://pypi.org/project/requests/)
4. [Youtube](https://www.youtube.com/results?search_query=python+networking+request+and+urllib)
5. [Google](https://www.google.com/search?q=python+networking+urllib+and+requests)

## Learning objectives

By the end of this project, you are expected to [explain to anyone]() **Without the help of Google**:

- [x] How to fetch internet resources with the Python package `urllib`
- [x] How to decode `urllib` body response
- [x] How to use the Python package `requests` #requestsiswaysimplerthanurllib
- [x] How to make HTTP `GET` request
- [x] How to make HTTP `POST/PUT`/etc. request
- [x] How to fetch JSON resources
- [x] How to manipulate data from an external service

## Tasks :page_with_curl:

- **0. What's my status? #0**

  - [0-hbtn_status.py](./0-hbtn_status.py): Python script that fetches
    `https://intranet.hbtn.io/status`.
  - Uses `urllib`.

* **1. Response header value #0**

  - [1-hbtn_header.py](./1-hbtn_header.py): Python script that displays the
    `X-Request-Id` response header variable of a request to a given URL.
  - Usage: `./1-hbtn_header.py <URL>`
  - Uses `urllib`.

* **2. POST an email #0**

  - [2-post_email.py](./2-post_email.py): Python script that sends a `POST`
    request to a given URL with a given email, and displays the response body.
  - Usage: `./2-post_email.py <URL> <email>`.
  - Uses `urllib`.

* **3. Error code #0**

  - [3-error_code.py](./3-error_code.py): Python script sends a request to
    a given URL and displays the response body.
  - Handles HTTP errors.
  - Uses `urllib`.

* **4. What's my status? #1**

  - [4-hbtn_status.py](./4-hbtn_status.py): Python script that fetches
    `https://intranet.hbtn.io/status`.
  - Uses `requests`.

* **5. Response header value #1**

  - [5-hbtn_header.py](./5-hbtn_header.py): Python script that displays the
    `X-Request-Id` response header variable of a request to a given URL.
  - Usage: `./5-hbtn_header.py <URL>`
  - Uses `requests`.
