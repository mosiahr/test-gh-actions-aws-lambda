# Test GitHub Actions

Status of Last Deployment:<br>
<img src="https://github.com/mosiahr/test-gh-actions-aws-lambda/workflows/CI/badge.svg?branch=main">


### Receiving data
I need to get data from MainTable table from Airtable. For this, I needed BaseId and api_key. Since there was only api_key, I copied the table to my account. I was using requests library to get data.


### Implementing a Circular Buffer
Here, I need to define a buffer with a fixed size. When it fills up, adding another element must overwrite the first (oldest) one.
