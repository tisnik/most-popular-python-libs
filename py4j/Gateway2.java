import py4j.GatewayServer;

public class Gateway2 {

    public String getMessage() {
        return "Hello from Java!";
    }

    public static void main(String[] args) {
        System.out.println("Starting gateway server");
        GatewayServer gatewayServer = new GatewayServer(new Gateway2());
        gatewayServer.start();
        System.out.println("gateway server started");
    }

}
