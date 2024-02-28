# End-to-end-hate-speech-NLP-project


## How to run?

```bash
conda create -n hate_speech python=3.8 -y
```

```bash
conda activate hate_speech 
```

```bash
pip install -r requirements.txt
```

## AWS setup  step by step for S3 bucket operations

- Create an AWS IAM Users -name >>>>hate_speech<<<< 
- Select AdministratorAccess
- Then Click on the hate_speech
- Then Click on the Security credentials 
- Then create an Access key 
- Download the access key
- Beyond The Follow below steps


```
setup AWS CLI
link: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```

```bash
aws configure
AWS_ACCESS_KEY_ID=***
AWS_SECRET_ACCESS_KEY= ***
AWS_REGION = us-east-1
```