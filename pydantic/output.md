# Weyland-Yutani Information System



## 🌍 Base URL


| URL | Description |
|-----|-------------|


# 🛠️ APIs

---

# 📋 Components



## Configuration


Global configuration.


| Field | Type | Description |
|-------|------|-------------|
| name | string | Service name |
| service |  | Service configuration |


## DatabaseConfiguration


Database configuration.


| Field | Type | Description |
|-------|------|-------------|
| host | string | Database server host or socket directory |
| port | integer | Database server port |
| db | string | Database name to connect to |
| user | string | Database user name used to authenticate |
| password | string | Password used to authenticate |
| ssl_mode | string | SSL mode |
| gss_encmode | string | This option determines whether or with what priority a secure GSS TCP/IP connection will be negotiated with the server. |
| ca_cert_path | string | Path to CA certificate |


## ServiceConfiguration


Service configuration.


| Field | Type | Description |
|-------|------|-------------|
| host | string | Service hostname |
| port | integer | Service port |
| auth_enabled | boolean | Enables authentication subsystem |
| workers | integer | Number of workers to be started |
| database |  | Database configuration |
