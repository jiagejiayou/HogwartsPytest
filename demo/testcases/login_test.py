from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLogin(HttpRunner):

    config = (Config("testcase description") \
        .verify(False)\
        .base_url("https://${host}")\
        .variables(#set gobal variables
        **{
                    "password": "xiaoniuer11",
                    "phone": "18628359732",
                    "host": "mubu.com",
                }
    )\
        .export("unreadCount","firstFolderId")#export导出参数后面调用
)
    teststeps = [
        Step(
            RunRequest("/login")
            .get("/login")
            .with_headers(
                **{
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Cookie": "_ga=GA1.2.728977736.1599662095; data_unique_id=d1e44655-5e65-4720-912e-9aece6f1369f; mubu_inner=1; csrf_token=892e56e3-15a3-46c7-a46d-56476a8e1f69; s_v_web_id=kf3y6bvj_GRvsHTIf_L7Sd_4WvY_9Fuk_K7N6wRZP9hLL; reg_entrance=https%3A%2F%2F${host}%2Flist; _gid=GA1.2.1134841487.1600173818; Hm_lvt_4426cbb0486a79ea049b4ad52d81b504=1599662193,1599875248,1600173818; language=en-US; country=US; reg_prepareId=17491d234a5-17491d234a0-4578-acd5-0429ec3e25cd; reg_focusId=4f90fb7c-cef8-4578-acd5-17491d239a9; SESSION=0ae21984-7c22-4e0d-b12e-e03790fe6ba3; _gat=1; Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504=1600174423; SLARDAR_WEB_ID=2f2dda9a-29b5-4a04-825a-a23c6ba6d3a4",
                    "Host": "${host}",
                    "Referer": "https://${host}/",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-User": "?1",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "foldersList":"$firstFolderId"
                }
            )
            .with_cookies(
                **{
                    "SESSION": "0ae21984-7c22-4e0d-b12e-e03790fe6ba3",
                    "country": "US",
                    "csrf_token": "892e56e3-15a3-46c7-a46d-56476a8e1f69",
                    "data_unique_id": "d1e44655-5e65-4720-912e-9aece6f1369f",
                    "language": "en-US",
                    "mubu_inner": "1",
                    "reg_entrance": "https%3A%2F%2F${host}%2Flist",
                    "reg_focusId": "4f90fb7c-cef8-4578-acd5-17491d239a9",
                    "reg_prepareId": "17491d234a5-17491d234a0-4578-acd5-0429ec3e25cd",
                    "s_v_web_id": "kf3y6bvj_GRvsHTIf_L7Sd_4WvY_9Fuk_K7N6wRZP9hLL",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "text/html;charset=UTF-8")
        ),
        Step(
            RunRequest("/login/password")
            .get("/login/password")
            .with_headers(
                **{
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Cookie": "_ga=GA1.2.728977736.1599662095; data_unique_id=d1e44655-5e65-4720-912e-9aece6f1369f; mubu_inner=1; csrf_token=892e56e3-15a3-46c7-a46d-56476a8e1f69; s_v_web_id=kf3y6bvj_GRvsHTIf_L7Sd_4WvY_9Fuk_K7N6wRZP9hLL; reg_entrance=https%3A%2F%2F${host}%2Flist; _gid=GA1.2.1134841487.1600173818; Hm_lvt_4426cbb0486a79ea049b4ad52d81b504=1599662193,1599875248,1600173818; language=en-US; country=US; SESSION=0ae21984-7c22-4e0d-b12e-e03790fe6ba3; _gat=1; SLARDAR_WEB_ID=90b0e644-0a9e-4112-ac4c-7a313d54f9bd; reg_prepareId=17491d42cdb-17491d42c59-4c16-a29d-314c8a065e9a; Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504=1600174436; reg_focusId=54c7d421-47a5-4c16-a29d-17491d430a9",
                    "Host": "${host}",
                    "Referer": "https://${host}/login",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-User": "?1",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                }
            )
            .with_cookies(
                **{
                    "SESSION": "0ae21984-7c22-4e0d-b12e-e03790fe6ba3",
                    "SLARDAR_WEB_ID": "90b0e644-0a9e-4112-ac4c-7a313d54f9bd",
                    "country": "US",
                    "csrf_token": "892e56e3-15a3-46c7-a46d-56476a8e1f69",
                    "data_unique_id": "d1e44655-5e65-4720-912e-9aece6f1369f",
                    "language": "en-US",
                    "mubu_inner": "1",
                    "reg_entrance": "https%3A%2F%2F${host}%2Flist",
                    "reg_focusId": "54c7d421-47a5-4c16-a29d-17491d430a9",
                    "reg_prepareId": "17491d42cdb-17491d42c59-4c16-a29d-314c8a065e9a",
                    "s_v_web_id": "kf3y6bvj_GRvsHTIf_L7Sd_4WvY_9Fuk_K7N6wRZP9hLL",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "text/html;charset=UTF-8")
        ),
        Step(
            RunRequest("/api/login/submit")
            #set local variables
            # .with_variables(
            #     **{
            #         "password": "xiaoniuer11",
            #         "phone": "18628359732"
            #     })
            .post("/api/login/submit")
            .with_headers(
                **{
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Length": "52",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Cookie": "_ga=GA1.2.728977736.1599662095; data_unique_id=d1e44655-5e65-4720-912e-9aece6f1369f; mubu_inner=1; csrf_token=892e56e3-15a3-46c7-a46d-56476a8e1f69; s_v_web_id=kf3y6bvj_GRvsHTIf_L7Sd_4WvY_9Fuk_K7N6wRZP9hLL; reg_entrance=https%3A%2F%2F${host}%2Flist; _gid=GA1.2.1134841487.1600173818; Hm_lvt_4426cbb0486a79ea049b4ad52d81b504=1599662193,1599875248,1600173818; language=en-US; country=US; SESSION=0ae21984-7c22-4e0d-b12e-e03790fe6ba3; _gat=1; reg_prepareId=17491d42cdb-17491d42c59-4c16-a29d-314c8a065e9a; reg_focusId=54c7d421-47a5-4c16-a29d-17491d430a9; Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504=1600174437; SLARDAR_WEB_ID=701da187-6f92-4859-b639-1bbb446e3b30",
                    "Host": "${host}",
                    "Origin": "https://${host}",
                    "Referer": "https://${host}/login/password",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "X-Requested-With": "XMLHttpRequest",
                }
            )
            .with_cookies(
                **{
                    "SESSION": "0ae21984-7c22-4e0d-b12e-e03790fe6ba3",
                    "SLARDAR_WEB_ID": "701da187-6f92-4859-b639-1bbb446e3b30",
                    "country": "US",
                    "csrf_token": "892e56e3-15a3-46c7-a46d-56476a8e1f69",
                    "data_unique_id": "d1e44655-5e65-4720-912e-9aece6f1369f",
                    "language": "en-US",
                    "mubu_inner": "1",
                    "reg_entrance": "https%3A%2F%2F${host}%2Flist",
                    "reg_focusId": "54c7d421-47a5-4c16-a29d-17491d430a9",
                    "reg_prepareId": "17491d42cdb-17491d42c59-4c16-a29d-314c8a065e9a",
                    "s_v_web_id": "kf3y6bvj_GRvsHTIf_L7Sd_4WvY_9Fuk_K7N6wRZP9hLL",
                }
            )
            .with_data(
                {"password": "${password}", "phone": "${phone}", "remember": "true"}
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
            .assert_equal("body.data.next", "/list")
            .assert_equal("body.msg", None)
        ),
        Step(
            RunRequest("/list")
            .get("/list")
            .with_headers(
                **{
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Cookie": "_ga=GA1.2.728977736.1599662095; data_unique_id=d1e44655-5e65-4720-912e-9aece6f1369f; mubu_inner=1; csrf_token=892e56e3-15a3-46c7-a46d-56476a8e1f69; s_v_web_id=kf3y6bvj_GRvsHTIf_L7Sd_4WvY_9Fuk_K7N6wRZP9hLL; reg_entrance=https%3A%2F%2F${host}%2Flist; _gid=GA1.2.1134841487.1600173818; Hm_lvt_4426cbb0486a79ea049b4ad52d81b504=1599662193,1599875248,1600173818; language=en-US; country=US; SESSION=0ae21984-7c22-4e0d-b12e-e03790fe6ba3; _gat=1; reg_prepareId=17491d42cdb-17491d42c59-4c16-a29d-314c8a065e9a; reg_focusId=54c7d421-47a5-4c16-a29d-17491d430a9; Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504=1600174437; SLARDAR_WEB_ID=701da187-6f92-4859-b639-1bbb446e3b30; Jwt-Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAxMDYwOCIsImV4cCI6MTYwMjc2NjQ0MywiaWF0IjoxNjAwMTc0NDQzfQ.VrdTGo1SPaiZ_sOln8uTGIIQwGiYsZJz7QslTrjXWc7DqXb4HproNercy9TxCbSBXtlE8dlft1eX0OpgU6na6A; user_persistence=bef4f285-6853-4476-bf6e-74cd85552cfa",
                    "Host": "${host}",
                    "Referer": "https://${host}/login/password",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-User": "?1",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                }
            )
            .with_cookies(
                **{
                    "Jwt-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAxMDYwOCIsImV4cCI6MTYwMjc2NjQ0MywiaWF0IjoxNjAwMTc0NDQzfQ.VrdTGo1SPaiZ_sOln8uTGIIQwGiYsZJz7QslTrjXWc7DqXb4HproNercy9TxCbSBXtlE8dlft1eX0OpgU6na6A",
                    "SESSION": "0ae21984-7c22-4e0d-b12e-e03790fe6ba3",
                    "SLARDAR_WEB_ID": "701da187-6f92-4859-b639-1bbb446e3b30",
                    "country": "US",
                    "csrf_token": "892e56e3-15a3-46c7-a46d-56476a8e1f69",
                    "data_unique_id": "d1e44655-5e65-4720-912e-9aece6f1369f",
                    "language": "en-US",
                    "mubu_inner": "1",
                    "reg_entrance": "https%3A%2F%2F${host}%2Flist",
                    "reg_focusId": "54c7d421-47a5-4c16-a29d-17491d430a9",
                    "reg_prepareId": "17491d42cdb-17491d42c59-4c16-a29d-314c8a065e9a",
                    "s_v_web_id": "kf3y6bvj_GRvsHTIf_L7Sd_4WvY_9Fuk_K7N6wRZP9hLL",
                    "user_persistence": "bef4f285-6853-4476-bf6e-74cd85552cfa",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "text/html;charset=UTF-8")
        ),
        Step(
            RunRequest("/api/list/tip_new_update")
            .post("/api/list/tip_new_update")
            .with_headers(
                **{
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Length": "0",
                    "Cookie": "_ga=GA1.2.728977736.1599662095; data_unique_id=d1e44655-5e65-4720-912e-9aece6f1369f; mubu_inner=1; csrf_token=892e56e3-15a3-46c7-a46d-56476a8e1f69; s_v_web_id=kf3y6bvj_GRvsHTIf_L7Sd_4WvY_9Fuk_K7N6wRZP9hLL; reg_entrance=https%3A%2F%2F${host}%2Flist; _gid=GA1.2.1134841487.1600173818; Hm_lvt_4426cbb0486a79ea049b4ad52d81b504=1599662193,1599875248,1600173818; language=en-US; country=US; SESSION=0ae21984-7c22-4e0d-b12e-e03790fe6ba3; _gat=1; reg_prepareId=17491d42cdb-17491d42c59-4c16-a29d-314c8a065e9a; reg_focusId=54c7d421-47a5-4c16-a29d-17491d430a9; Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504=1600174437; SLARDAR_WEB_ID=701da187-6f92-4859-b639-1bbb446e3b30; Jwt-Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAxMDYwOCIsImV4cCI6MTYwMjc2NjQ0MywiaWF0IjoxNjAwMTc0NDQzfQ.VrdTGo1SPaiZ_sOln8uTGIIQwGiYsZJz7QslTrjXWc7DqXb4HproNercy9TxCbSBXtlE8dlft1eX0OpgU6na6A; user_persistence=bef4f285-6853-4476-bf6e-74cd85552cfa",
                    "Host": "${host}",
                    "Origin": "https://${host}",
                    "Referer": "https://${host}/list",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "X-Requested-With": "XMLHttpRequest",
                }
            )
            .with_cookies(
                **{
                    "Jwt-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAxMDYwOCIsImV4cCI6MTYwMjc2NjQ0MywiaWF0IjoxNjAwMTc0NDQzfQ.VrdTGo1SPaiZ_sOln8uTGIIQwGiYsZJz7QslTrjXWc7DqXb4HproNercy9TxCbSBXtlE8dlft1eX0OpgU6na6A",
                    "SESSION": "0ae21984-7c22-4e0d-b12e-e03790fe6ba3",
                    "SLARDAR_WEB_ID": "701da187-6f92-4859-b639-1bbb446e3b30",
                    "country": "US",
                    "csrf_token": "892e56e3-15a3-46c7-a46d-56476a8e1f69",
                    "data_unique_id": "d1e44655-5e65-4720-912e-9aece6f1369f",
                    "language": "en-US",
                    "mubu_inner": "1",
                    "reg_entrance": "https%3A%2F%2F${host}%2Flist",
                    "reg_focusId": "54c7d421-47a5-4c16-a29d-17491d430a9",
                    "reg_prepareId": "17491d42cdb-17491d42c59-4c16-a29d-314c8a065e9a",
                    "s_v_web_id": "kf3y6bvj_GRvsHTIf_L7Sd_4WvY_9Fuk_K7N6wRZP9hLL",
                    "user_persistence": "bef4f285-6853-4476-bf6e-74cd85552cfa",
                }
            )
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
        ),
        Step(
            RunRequest("/api/list/get")
            .post("/api/list/get")
            .with_headers(
                **{
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Length": "38",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Cookie": "_ga=GA1.2.728977736.1599662095; data_unique_id=d1e44655-5e65-4720-912e-9aece6f1369f; mubu_inner=1; csrf_token=892e56e3-15a3-46c7-a46d-56476a8e1f69; s_v_web_id=kf3y6bvj_GRvsHTIf_L7Sd_4WvY_9Fuk_K7N6wRZP9hLL; reg_entrance=https%3A%2F%2F${host}%2Flist; _gid=GA1.2.1134841487.1600173818; Hm_lvt_4426cbb0486a79ea049b4ad52d81b504=1599662193,1599875248,1600173818; language=en-US; country=US; SESSION=0ae21984-7c22-4e0d-b12e-e03790fe6ba3; _gat=1; reg_prepareId=17491d42cdb-17491d42c59-4c16-a29d-314c8a065e9a; reg_focusId=54c7d421-47a5-4c16-a29d-17491d430a9; Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504=1600174437; SLARDAR_WEB_ID=701da187-6f92-4859-b639-1bbb446e3b30; Jwt-Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAxMDYwOCIsImV4cCI6MTYwMjc2NjQ0MywiaWF0IjoxNjAwMTc0NDQzfQ.VrdTGo1SPaiZ_sOln8uTGIIQwGiYsZJz7QslTrjXWc7DqXb4HproNercy9TxCbSBXtlE8dlft1eX0OpgU6na6A; user_persistence=bef4f285-6853-4476-bf6e-74cd85552cfa",
                    "Host": "${host}",
                    "Origin": "https://${host}",
                    "Referer": "https://${host}/list",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "X-Requested-With": "XMLHttpRequest",
                }
            )
            .with_cookies(
                **{
                    "Jwt-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAxMDYwOCIsImV4cCI6MTYwMjc2NjQ0MywiaWF0IjoxNjAwMTc0NDQzfQ.VrdTGo1SPaiZ_sOln8uTGIIQwGiYsZJz7QslTrjXWc7DqXb4HproNercy9TxCbSBXtlE8dlft1eX0OpgU6na6A",
                    "SESSION": "0ae21984-7c22-4e0d-b12e-e03790fe6ba3",
                    "SLARDAR_WEB_ID": "701da187-6f92-4859-b639-1bbb446e3b30",
                    "country": "US",
                    "csrf_token": "892e56e3-15a3-46c7-a46d-56476a8e1f69",
                    "data_unique_id": "d1e44655-5e65-4720-912e-9aece6f1369f",
                    "language": "en-US",
                    "mubu_inner": "1",
                    "reg_entrance": "https%3A%2F%2F${host}%2Flist",
                    "reg_focusId": "54c7d421-47a5-4c16-a29d-17491d430a9",
                    "reg_prepareId": "17491d42cdb-17491d42c59-4c16-a29d-314c8a065e9a",
                    "s_v_web_id": "kf3y6bvj_GRvsHTIf_L7Sd_4WvY_9Fuk_K7N6wRZP9hLL",
                    "user_persistence": "bef4f285-6853-4476-bf6e-74cd85552cfa",
                }
            )
            .with_data({"folderId": "0", "keywords": "", "sort": "time", "source": ""})
            .teardown_hook("${get_folders_num($response)}", "foldersNum")
            .extract()
            .with_jmespath("body.data.folders","foldersList")
            .with_jmespath("body.data.folders[0].id","firstFolderId")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
            .assert_length_greater_than("$foldersList",3)
            .assert_greater_than("$foldersNum",3)
        ),
        Step(
            RunRequest("/api/message/get_message_unread")
            .post("/api/message/get_message_unread")
            .with_headers(
                **{
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Length": "0",
                    "Cookie": "_ga=GA1.2.728977736.1599662095; data_unique_id=d1e44655-5e65-4720-912e-9aece6f1369f; mubu_inner=1; csrf_token=892e56e3-15a3-46c7-a46d-56476a8e1f69; s_v_web_id=kf3y6bvj_GRvsHTIf_L7Sd_4WvY_9Fuk_K7N6wRZP9hLL; reg_entrance=https%3A%2F%2F${host}%2Flist; _gid=GA1.2.1134841487.1600173818; Hm_lvt_4426cbb0486a79ea049b4ad52d81b504=1599662193,1599875248,1600173818; language=en-US; country=US; SESSION=0ae21984-7c22-4e0d-b12e-e03790fe6ba3; _gat=1; reg_prepareId=17491d42cdb-17491d42c59-4c16-a29d-314c8a065e9a; reg_focusId=54c7d421-47a5-4c16-a29d-17491d430a9; Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504=1600174437; SLARDAR_WEB_ID=701da187-6f92-4859-b639-1bbb446e3b30; Jwt-Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAxMDYwOCIsImV4cCI6MTYwMjc2NjQ0MywiaWF0IjoxNjAwMTc0NDQzfQ.VrdTGo1SPaiZ_sOln8uTGIIQwGiYsZJz7QslTrjXWc7DqXb4HproNercy9TxCbSBXtlE8dlft1eX0OpgU6na6A; user_persistence=bef4f285-6853-4476-bf6e-74cd85552cfa",
                    "Host": "${host}",
                    "Origin": "https://${host}",
                    "Referer": "https://${host}/list",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "X-Requested-With": "XMLHttpRequest",
                }
            )
            .with_cookies(
                **{
                    "Jwt-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAxMDYwOCIsImV4cCI6MTYwMjc2NjQ0MywiaWF0IjoxNjAwMTc0NDQzfQ.VrdTGo1SPaiZ_sOln8uTGIIQwGiYsZJz7QslTrjXWc7DqXb4HproNercy9TxCbSBXtlE8dlft1eX0OpgU6na6A",
                    "SESSION": "0ae21984-7c22-4e0d-b12e-e03790fe6ba3",
                    "SLARDAR_WEB_ID": "701da187-6f92-4859-b639-1bbb446e3b30",
                    "country": "US",
                    "csrf_token": "892e56e3-15a3-46c7-a46d-56476a8e1f69",
                    "data_unique_id": "d1e44655-5e65-4720-912e-9aece6f1369f",
                    "language": "en-US",
                    "mubu_inner": "1",
                    "reg_entrance": "https%3A%2F%2F${host}%2Flist",
                    "reg_focusId": "54c7d421-47a5-4c16-a29d-17491d430a9",
                    "reg_prepareId": "17491d42cdb-17491d42c59-4c16-a29d-314c8a065e9a",
                    "s_v_web_id": "kf3y6bvj_GRvsHTIf_L7Sd_4WvY_9Fuk_K7N6wRZP9hLL",
                    "user_persistence": "bef4f285-6853-4476-bf6e-74cd85552cfa",
                }
            )
            .with_data("")
            .extract()
            .with_jmespath("body.data.unreadCount","unreadCount")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
        ),
    ]


if __name__ == "__main__":
    TestCaseLogin().test_start()
