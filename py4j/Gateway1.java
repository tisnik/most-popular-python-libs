import py4j.GatewayServer;

public class Gateway1 {

    public static void main(String[] args) {
        System.out.println("Starting gateway server");
        GatewayServer gatewayServer = new GatewayServer(new Gateway1());
        gatewayServer.start();
        System.out.println("gateway server started");
    }

}
