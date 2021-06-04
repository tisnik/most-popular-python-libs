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
