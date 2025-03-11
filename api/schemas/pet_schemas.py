create_pet = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "number"
        },
        "name": {
            "type": "string"
        },
        "photoUrls": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "number"
                    },
                    "name": {
                        "type": "string"
                    }
                },
                "required": [
                    "id",
                    "name"
                ]
            }
        }
    },
    "required": [
        "id",
        "name",
        "photoUrls",
        "tags"
    ]
}

get_pets_status = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "number"
      },
      "category": {
        "type": "object",
        "properties": {
          "id": {
            "type": "number"
          },
          "name": {
            "type": "string"
          }
        },
        "required": [
          "id"
        ]
      },
      "name": {
        "type": "string"
      },
      "photoUrls": {
        "type": "array",
        "items": {
          "type": ["string", "None"]
        }
      },
      "tags": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "id": {
              "type": "number"
            },
            "name": {
              "type": "string"
            }
          },
          "required": [
            "id"
          ]
        }
      },
      "status": {
        "type": "string",
        "enum": ["available", "pending", "sold"]
      }
    },
    "required": [
      "id",
      "photoUrls",
      "tags",
      "status"
    ]
  }
}

get_pet_negative = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "code": {
      "type": "number",
      "enum": [1]
    },
    "type": {
      "type": "string",
      "enum": ["error"]
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "code",
    "type",
    "message"
  ]
}

delete_pet = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "code": {
      "type": "number"
    },
    "type": {
      "type": "string",
      "enum": ["unknown"]
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "code",
    "type",
    "message"
  ]
}