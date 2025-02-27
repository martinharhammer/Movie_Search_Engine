# Elasticsearch setup guide

## Install Elasticsearch

You can find the official installation [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html). Below, we summarized the necessary steps for Linux and Windows machines. 

### Linux

```bash
# Download and install the public signing key:
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg

# Install apt-transport-https (in case it's not already on your computer):
sudo apt-get install apt-transport-https

# Save the repository definition to /etc/apt/sources.list.d/elastic-8.x.list:
echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list

# Install the Elasticsearch Debian package:
sudo apt-get update && sudo apt-get install elasticsearch
```

### Windows

Download the `.zip` archive for Elasticsearch 8.4.3 from 
[here](https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.4.3-windows-x86_64.zip).

Extract the files. This folder will be referred to as `%ES_HOME%`.

Change into the `%ES_HOME%` folder and install Elasticsearch as a service:

```bash
.\bin\elasticsearch-service.bat install
```


## Disable security

### Linux

Open `elasticsearch.yml` for editing, e.g. with `vi`:
```bash
sudo vi /etc/elasticsearch/elasticsearch.yml
```

Set `xpack.security.enabled` to `false`:
```bash
xpack.security.enabled: false
```

Add `xpack.license.self_generated.type` field with value `basic`:
```bash
xpack.license.self_generated.type: basic
```

If you opened the file with `vi`, hit <Esc>, then type `:x`. This will save the modifications and close the file.

### Windows

Open the `%ES_HOME%\config\elasticsearch.yml` file with your favourite text editor.

Set `xpack.security.enabled` to `false` (or add if not yet there):
```bash
xpack.security.enabled: false
```

Add `xpack.license.self_generated.type` field with value `basic`:
```bash
xpack.license.self_generated.type: basic
```

## Start Elasticsearch

### Linux

```bash
sudo systemctl start elasticsearch.service
```

You can stop Elasticsearch by calling:

```bash
sudo systemctl stop elasticsearch.service
```

### Windows

Change to `%ES_HOME%`.

```bash
.\bin\elasticsearch-service.bat start
```

You can stop Elasticsearch by calling:

```bash
.\bin\elasticsearch-service.bat stop
```

## Check if elasticsearch is running

```bash
curl --verbose --show-error http://localhost:9200
```

You should see a similar answer:

```bash
*   Trying 127.0.0.1:9200...
* Connected to localhost (127.0.0.1) port 9200 (#0)
> GET / HTTP/1.1
> Host: localhost:9200
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< X-elastic-product: Elasticsearch
< content-type: application/json
< content-length: 529
< 
{
  "name" : "eszter",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "0RRJZz9ORciJOnDHM34MFA",
  "version" : {
    "number" : "8.4.3",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "42f05b9372a9a4a470db3b52817899b99a76ee73",
    "build_date" : "2022-10-04T07:17:24.662462378Z",
    "build_snapshot" : false,
    "lucene_version" : "9.3.0",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
* Connection #0 to host localhost left intact
```
