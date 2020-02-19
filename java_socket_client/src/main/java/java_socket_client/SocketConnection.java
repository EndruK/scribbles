package java_socket_client;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

public class SocketConnection {
    private Socket socket;
    private String ip;
    private int port;
    private BufferedReader in;
    private PrintWriter out;

    public SocketConnection(String ip, int port) {
        this.ip = ip;
        this.port = port;
    }

    public void connect() throws IOException {
        this.socket = new Socket(this.ip, this.port);
        this.in = new BufferedReader(new InputStreamReader(this.socket.getInputStream()));
        this.out = new PrintWriter(this.socket.getOutputStream(), true);
    }
    public void disconnect() throws IOException {
        this.in.close();
        this.out.close();
        this.socket.close();
    }

//    public void startConnection(String ip, int port) throws UnknownHostException, IOException {
//        socket = new Socket(ip, port);
//        out = new PrintWriter(socket.getOutputStream(), true);
//        in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
//    }

    public void sendMessage(String msg) throws IOException {
//        PrintWriter out = new PrintWriter(this.socket.getOutputStream(), true);
        out.println(msg);
        System.out.println("message was send to server");
    }

    public String receiveMessage() throws IOException  {
//        BufferedReader in = new BufferedReader(new InputStreamReader(this.socket.getInputStream()));
        System.out.println("getting response");
        boolean asd = in.ready();
        String line = "";
        String response = "";
        while(!(line = in.readLine()).equals("$EOS$")) {
            response += line + "\n";
        }
        return response;
    }
}
