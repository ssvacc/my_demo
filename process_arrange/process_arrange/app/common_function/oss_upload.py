import oss2
from ReturnEnum import ReturnEnum

from Project.settings import ACCESS_KEY_SECRET, ACCESS_KEY_ID, ENDPOINT, BUCKETNAME_DOWNLOAD, PREFIX, ENDPOINT_OUT
def f_UploadFileToOss(v_oss_path: str, v_file_name: str, v_file_object: object, v_bucket_name="") -> dict:
    result = {"code": ReturnEnum.ER_LOGISTICS_SECTION_CFG_FILE_UPLOAD().code,
              "msg": ReturnEnum.ER_LOGISTICS_SECTION_CFG_FILE_UPLOAD().msg,
              "data": dict()}
    try:
        _prefix = PREFIX
        _endpoint = ENDPOINT
        _endpoint_out = ENDPOINT_OUT
        _access_key_id = ACCESS_KEY_ID
        _access_key_secret = ACCESS_KEY_SECRET
        _bucket_name = BUCKETNAME_DOWNLOAD if not v_bucket_name else v_bucket_name

        auth = oss2.Auth(_access_key_id, _access_key_secret)
        bucket = oss2.Bucket(auth, _endpoint, _bucket_name)
        bucket.create_bucket(oss2.BUCKET_ACL_PUBLIC_READ)
        bucket.put_object(u'%s/%s' % (v_oss_path, v_file_name), v_file_object)
        result["code"] = ReturnEnum.ER_SUCCESS().code
        result["msg"] = ReturnEnum.ER_SUCCESS().msg
        result["data"] = {
            "v_oss_url": f"{_prefix}{_bucket_name}.{_endpoint_out}/{v_oss_path}/{v_file_name}"
        }
    except Exception as ex:
        result["msg"] = str(ex)
    return result