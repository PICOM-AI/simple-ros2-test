SOCKET_SERVER_HOST="127.0.0.1"
docker run -it --rm --network host -e HOST=$SOCKET_SERVER_HOST json-socket-sub