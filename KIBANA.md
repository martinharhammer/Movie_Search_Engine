# Kibana guide

Kibana provides a user-friendly Dev Console to send directly requests to you elasticsearch cluster. It cna help you prototype queries and quickly test your system. 

## Install Kibana

Follow [this](https://www.elastic.co/guide/en/kibana/current/install.html) guideline.

### Linux

Install Kibana from the APT repository:

```bash
sudo apt-get update && sudo apt-get install kibana
```

### Windows

Download the `.zip` archive for Kibana 8.4.3 from 
[here](https://artifacts.elastic.co/downloads/kibana/kibana-8.4.3-windows-x86_64.zip).

Extract the files. This folder will be referred to as `%KIBANA_HOME%`.

## Start Kibana

### Linux

```bash
sudo systemctl start kibana.service
```

You can reach Kibana from your browser under `http://localhost:5601`. (This usually takes a minute.)

You can stop Kibana by calling:

```bash
sudo systemctl stop kibana.service
```

### Windows

Change into the `%KIBANA_HOME%` folder and run the following command:

```bash
.\bin\kibana.bat
```

## Debug with Dev Tools

Open Kibana from your browser: http://localhost:5601.

From the hamburger menu choose Management -> Dev Tools. You will see the Console.

### Get all documents in the index

```bash
# Get the index
GET /demo_index

# Get all docs in index
GET movies_index/_search?scroll=1m
{
  "query": {
    "match_all": {}
  }
}
```

### Filter fields and use variables

With the `_source` field, you can define which fields of the document should be returned.
You can also define variables by clicking "Variables" on the upper left part. After defining one, you can use it the in queries:

```bash
GET movies_index/_search?scroll=1m
{
  "_source": ["title", "summary"], 
  "query": {
    "match": {
      "text": "${text}"
    }
  }
}
```

### Get score explanation

You can let ES explain to you how the score for a specific query and for a specific document is calculated. In the url you have to refer the documents by its id, which is the title of the wikipedia page. Beware that you have to replace spaces and special characters by using the [HTML URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.ASP).

```bash
GET movies_index/_explain/Gladiator%20(2000%20film)
{
  "query": {
    "match": {
      "title": "Gladiator"
    }
  }
}
```

### Analyze search query for field

```bash
POST movies_index/_analyze
{
  "field": "title", 
  "text": "Gladiator"
}
```
