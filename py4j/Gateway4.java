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
    public int add(int x, int y) {
        return x+y;
    }

    public double fadd(double x, double y) {
        return x+y;
    }

    public String sadd(String x, String y) {
        return x+y;
    }

    public List<String> aList(String first, String second) {
        List<String> list = new ArrayList<String>();
        list.add(first);
        list.add(second);
        return list;
    }

    public Map<String, String> aMap(String key, String value) {
        Map<String, String> map = new HashMap<String, String>();
        map.put(key, value);
        map.put("foo", "bar");
        map.put("bar", "baz");
        return map;
    }

    public String getMessage() {
        return "Hello from entrypoint #1";
    }
}

public class Gateway4 {

    public static void main(String[] args) {
        System.out.println("Starting gateway server");

        GatewayServer gatewayServer1 = new GatewayServer(new EntryPoint1(), 20001);
        gatewayServer1.start();

        System.out.println("gateway server started");
    }

}
