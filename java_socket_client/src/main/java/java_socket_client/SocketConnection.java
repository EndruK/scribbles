package java_socket_client;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

public class SocketConnection {
    private Socket socket;
    private PrintWriter out;
    private BufferedReader in;

    public void startConnection(String ip, int port) throws UnknownHostException, IOException {
        socket = new Socket(ip, port);
        out = new PrintWriter(socket.getOutputStream(), true);
        in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
    }

    public String sendMessage(String msg) throws IOException {
        out.println(msg);
        String line = "";
        String response = "";
        while(!(line = in.readLine()).equals("$EOS$")) {
            response += line + "\n";
        }
        return response;
    }

    public void stopConnection() throws IOException {
        in.close();
        out.close();
        socket.close();
    }
}
