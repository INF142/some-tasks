## Run the clients and the server with docker compose

In the terminal, make sure you are in the folder containing `docker-compose.yml`. Then, run

```sh
docker compose up
```
For each client:
- Open another tab in the terminal in the same folder as before.
- Run
    ```sh
    docker compose exec <client name> bash
    ```
    *NB*: Replace `<client name>` by `client1`, `client2` or `client3`, accordingly.
- Run
    ```sh
    python chat_client.py
    ```
