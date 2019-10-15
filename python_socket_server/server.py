#!/usr/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 8101

class Server:
    s: socket.socket

    def __init__(self, host, port) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))

    def start_server(self) -> None:
        self.s.listen()
        print("server started and listening on port ", self.s.getsockname())

    def send_message(self, connection, message) -> None:
        # append $EOS$
        message += "\n$EOS$"
        connection.sendall(str.encode(message))
        connection.close()

    def get_message(self):
        conn, addr = self.s.accept()
        print("connection received by ", addr)
        data = conn.recv(1024)
        return data, conn


if __name__ == "__main__":
    s = Server(HOST, PORT)
    s.start_server()
    while True:
        data, conn = s.get_message()
        print(bytes.decode(data))
        text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ullamcorper a lacus vestibulum sed arcu non odio. Ut tellus elementum sagittis vitae et. Interdum posuere lorem ipsum dolor sit amet. Ut pharetra sit amet aliquam. A arcu cursus vitae congue mauris rhoncus aenean. Tristique senectus et netus et malesuada fames. Arcu bibendum at varius vel pharetra vel turpis nunc eget. Ut faucibus pulvinar elementum integer enim neque. In mollis nunc sed id semper risus in. Auctor eu augue ut lectus arcu bibendum. Orci eu lobortis elementum nibh tellus. Magna etiam tempor orci eu. Diam volutpat commodo sed egestas egestas fringilla phasellus faucibus. Maecenas accumsan lacus vel facilisis volutpat est velit.

Quam adipiscing vitae proin sagittis nisl. In nisl nisi scelerisque eu. Duis ultricies lacus sed turpis tincidunt id aliquet risus. Sit amet aliquam id diam maecenas ultricies mi. Id porta nibh venenatis cras. Congue quisque egestas diam in. Odio ut enim blandit volutpat maecenas volutpat blandit. Quam adipiscing vitae proin sagittis nisl rhoncus mattis. Orci porta non pulvinar neque laoreet suspendisse interdum consectetur libero. In massa tempor nec feugiat nisl pretium. Id interdum velit laoreet id donec.

Sollicitudin aliquam ultrices sagittis orci a scelerisque purus semper. Nam aliquam sem et tortor consequat id porta nibh venenatis. Condimentum lacinia quis vel eros donec ac odio tempor orci. In egestas erat imperdiet sed euismod nisi porta lorem. Id diam vel quam elementum pulvinar etiam non quam. Aliquam ut porttitor leo a diam sollicitudin. Sed elementum tempus egestas sed sed risus pretium. Bibendum ut tristique et egestas quis ipsum suspendisse. Maecenas sed enim ut sem viverra aliquet eget. Semper viverra nam libero justo. Vitae suscipit tellus mauris a diam maecenas sed enim. A iaculis at erat pellentesque adipiscing commodo elit at imperdiet. Vestibulum rhoncus est pellentesque elit ullamcorper. Sed odio morbi quis commodo odio. Arcu cursus vitae congue mauris. Aliquet nibh praesent tristique magna sit amet purus gravida. Neque volutpat ac tincidunt vitae semper quis lectus nulla at. Habitant morbi tristique senectus et netus et malesuada fames ac. Vestibulum morbi blandit cursus risus at. Nibh mauris cursus mattis molestie a iaculis at erat pellentesque.

Id consectetur purus ut faucibus pulvinar elementum integer enim neque. Eu lobortis elementum nibh tellus molestie nunc. Orci porta non pulvinar neque laoreet suspendisse interdum consectetur. Faucibus et molestie ac feugiat sed lectus vestibulum mattis ullamcorper. Suspendisse sed nisi lacus sed viverra. Morbi blandit cursus risus at ultrices mi tempus. Vel eros donec ac odio. Urna nec tincidunt praesent semper feugiat nibh sed pulvinar. Diam maecenas sed enim ut sem. Non nisi est sit amet facilisis magna. Condimentum vitae sapien pellentesque habitant morbi tristique senectus et netus.

Mi bibendum neque egestas congue quisque egestas diam. Integer quis auctor elit sed vulputate mi sit amet. Sed risus ultricies tristique nulla aliquet enim tortor. Malesuada fames ac turpis egestas integer eget aliquet. Neque sodales ut etiam sit amet nisl purus in. Nisl nisi scelerisque eu ultrices vitae auctor eu augue ut. Luctus accumsan tortor posuere ac ut consequat semper viverra nam. Vel elit scelerisque mauris pellentesque pulvinar pellentesque. In cursus turpis massa tincidunt dui ut ornare lectus. Eu non diam phasellus vestibulum lorem sed risus ultricies tristique. In fermentum posuere urna nec tincidunt praesent. Semper auctor neque vitae tempus quam pellentesque nec. Placerat in egestas erat imperdiet sed euismod nisi. Gravida quis blandit turpis cursus in hac. Lectus nulla at volutpat diam ut. Faucibus a pellentesque sit amet porttitor eget dolor morbi non. Amet aliquam id diam maecenas ultricies mi eget mauris. Risus nec feugiat in fermentum. Elementum pulvinar etiam non quam lacus.
        """
        s.send_message(conn, text)