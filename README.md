# S3 migrate to GCS

檢查 S3 Bucket 有新增檔案時觸發 lambda 將檔案同步到 GCS Bucket

![Flow](/images/flow.jpg)


### Env
 - Python 3.7
 - [Poetry](https://github.com/python-poetry/poetry)
 - [Chalice](https://github.com/aws/chalice)


### Setup

1. 從 config.example.json 複製一份 config.json，並填入 S3 bucket 和 GCS bucket

   ```
   cp .chalice/config.example.json .chalice/config.json
   ```

2. 將 GCS credentail 放入 /chalicelib/gcs_credential/service_account.json

3. Install python package

   ```
   $ python --version
   > Python 3.7.7

   $ pip install -r requirements
   ```

4. Deploy to AWS Lambda

   ```
   $ python -m chalice deploy
   ```
