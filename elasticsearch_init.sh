# we create elasticsearch index relations with a single type relation
curl -X PUT -H "Authorization: Basic ZWxhc3RpYzpjaGFuZ2VtZQ==" -H "Content-Type: application/json" -H "Cache-Control: no-cache" -d '{
	"mappings": {
	    "relation": {
	      "properties": {
	        "mot1":  { "type": "text", "analyzer": "french" },
	        "mot2":  { "type": "text", "analyzer": "french"  },
	        "relation":  { "type": "integer" },
	        "poids": { "type": "integer"}
	      }
	    }
    }
}' "http://localhost:9200/relations"

# we encode the original corpus in utf8
iconv -f latin1 -t utf8 $1 > relations_utf8.txt

# we index all relations
python index_relations.py
