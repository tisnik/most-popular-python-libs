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

import java.util.*;

class EntryPoint1 {

    Map<String, String> aMap = new HashMap<String, String>();

    public Map<String, String> getMap() {
        return this.aMap;
    }

    public void printMap() {
        System.out.println("Map seen on Java side:");

        for (Map.Entry<String, String> item: this.aMap.entrySet()) {
            System.out.format("key: %s,  value: %s\n", item.getKey(), item.getValue());
        }

        System.out.println();
    }
}

public class Gateway5 {

    public static void main(String[] args) {
        System.out.println("Starting gateway server");

        GatewayServer gatewayServer1 = new GatewayServer(new EntryPoint1(), 20001);
        gatewayServer1.start();

        System.out.println("gateway server started");
    }

}
