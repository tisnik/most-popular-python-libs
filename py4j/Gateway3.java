//
//  (C) Copyright 2021  Pavel Tisnovsky
//
//  All rights reserved. This program and the accompanying materials
//  are made available under the terms of the Eclipse Public License v1.0
//  which accompanies this distribution, and is available at
//  http://www.eclipse.org/legal/epl-v10.html
//
//  Contributors:
//      Pavel Tisnovsky
//

import py4j.GatewayServer;

class EntryPoint1 {
    public String getMessage() {
        return "Hello from entrypoint #1";
    }
}

class EntryPoint2 {
    public String getMessage() {
        return "Hello from entrypoint #2";
    }
}

public class Gateway3 {

    public static void main(String[] args) {
        System.out.println("Starting two gateway servers");

        GatewayServer gatewayServer1 = new GatewayServer(new EntryPoint1(), 20001);
        gatewayServer1.start();

        GatewayServer gatewayServer2 = new GatewayServer(new EntryPoint2(), 20002);
        gatewayServer2.start();

        System.out.println("gateway servers started");
    }

}
