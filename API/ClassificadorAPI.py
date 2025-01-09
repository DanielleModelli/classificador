# from app import app, mongo
# from bson.json_util import dumps
# from bson.objectid import ObjectId
# from flask import Flask, jsonify, request

# app = Flask(__name__)


# @app.route("api/vetor_porcentagem", methods=['GET'])
# def users():
# 	vetor_porcentagem = mongo.db.user.find()
# 	resp = dumps(vetor_porcentagem)
# 	return resp

# @app.route("/api/v1/vetor_porcentagem", methods=['GET'])
# def get_vetor_porcentagem():
#     """
#        Function to get the vetor_porcentagem from robo 3t.
#        """
#     try:
#         # Call the function to get the query params
#         query_params = helper_module.parse_query_params(request.query_string)
#         # Check if dictionary is not empty
#         if query_params:

#             # Try to convert the value to int
#             query = {k: int(v) if isinstance(v, str) and v.isdigit() else v for k, v in query_params.items()}

#             # Fetch all the record(s)
#             records_fetched = collection.find(query)

#             # Check if the records are found
#             if records_fetched.count() > 0:
#                 # Prepare the response
#                 return dumps(records_fetched)
#             else:
#                 # No records are found
#                 return "", 404

#         # If dictionary is empty
#         else:
#             # Return all the records as query string parameters are not available
#             if collection.find().count > 0:
#                 # Prepare response if the users are found
#                 return dumps(collection.find())
#             else:
#                 # Return empty array if no users are found
#                 return jsonify([])
#     except:
#         # Error while trying to fetch the resource
#         # Add message for debugging purpose
#         return "", 500


# if __name__ == '__main__':
#      app.run()