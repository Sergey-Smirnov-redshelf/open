import urllib.request

# This variable contains a request to 'http: // localhost: 1234 /'.
fp = urllib.request.urlopen("http://localhost:1111/")

# 'encodedContent' matches the encoded server response ('index.html').
# 'decodedContent' matches the decoded server response (this is what we want to display).
encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")

# Display the contents of the file received from the server ('index.html').
print(decodedContent)

# Close the connection to the server.
fp.close()