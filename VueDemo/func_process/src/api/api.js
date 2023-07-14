// api
APPROVE_PERSON = '/func_process_app/public_user_info/is_approve_person' // 用户名
// 参数
PARAM_PAGE = '/func_process_app/public_params/page' // 参数列表查询
PARAM_CHILD_PAGE = '/func_process_app/public_params/page_child' // 参数列表包含子参数查询
PARAM_LIST = '/func_process_app/public_params/paramlist' // 参数列表滚动查询
PARAM_CHILD = '/func_process_app/public_params/childParam' // 查询子参数
PARAM_BY_IDLIST = '/func_process_app/public_params/getByIdList' // 根据id列表查询参数
PARAM_ADD = '/func_process_app/public_params/add' // 新增参数
PARAM_EDIT = '/func_process_app/public_params/update' // 根据id修改参数
PARAM_DEL = '/func_process_app/public_params/del' // 根据id删除参数
PARAM_COMMIT = '/func_process_app/public_params/commit' // 提交参数
PARAM_APPROVE = '/func_process_app/public_params/approve' // 审批参数

// 返回码
ERROR_CODE_LIST = '/func_process_app/public_error_code/list' // 返回码列表滚动查询
ERROR_CODE_ADD = '/func_process_app/public_error_code/add' // 新增返回码
ERROR_CODE_EDIT = '/func_process_app/public_error_code/update' // 根据id修改返回码
ERROR_CODE_DEL = '/func_process_app/public_error_code/del' // 根据id删除返回码
ERROR_CODE_BYTASKID = '/func_process_app/public_custom_function/getErrorCode' // 查询流程返回码

// 类名
CLASS_ADD = '/func_process_app/public_class/add' // 新增类
CLASS_EDIT = '/func_process_app/public_class/edit' // 修改类
CLASS_DEL = '/func_process_app/public_class/del' // 删除类
CLASS_LIST = '/func_process_app/public_class/list' // 类列表

// 函数
FUNCTION_LIST = '/func_process_app/public_function/list' // 函数列表查询
FUNCTION_SIMPLE_LIST = '/func_process_app/public_function/simpleList' // 函数列表查询
FUNCTION_ADD = '/func_process_app/public_function/add' // 新增函数
FUNCTION_EDIT = '/func_process_app/public_function/update' // 根据id修改函数
FUNCTION_DEL = '/func_process_app/public_function/del' // 根据id删除函数
FUNCTION_RUN = '/func_process_app/public_function/runFunction' // 函数调试
FUNCTION_SHOW = '/func_process_app/public_function/showFunction' // 展示函数体
FUNCTION_COMMIT = '/func_process_app/public_function/commit' // 提交函数
FUNCTION_APPROVE = '/func_process_app/public_function/approve' // 审批函数
FUNCTION_REVIEW = '/func_process_app/public_function/review' // review函数
FUNCTION_DEVELOP = '/func_process_app/public_function/develop' // 驳回开发函数
FUNCTION_TOTEST = '/func_process_app/public_function/toTest' // 转测试函数
FUNCTION_PUBLISH = '/func_process_app/public_function/publish' // 发布函数
FUNCTION_ADD_AUTO_TEST = '/func_process_app/public_function/add_auto_test' // 加入自动化测试
FUNCTION_COUNT = '/func_process_app/public_function/function_count' // 加入自动化测试

// 函数参数
FUNC_PARAM_BYFUNID = '/func_process_app/fun_param/getByFunId' // 根据函数id查询参数和返回值
CUSTOM_PARAM_BY_FUNCLIST = '/func_process_app/fun_param/getByFunListId' // 功能配置根据函数id查询参数和返回值
// 函数组合
CUSTOM_LIST = '/func_process_app/public_custom_function/list' // 功能列表查询
CUSTOM_ADD = '/func_process_app/public_custom_function/add' // 新增功能
CUSTOM_EDIT = '/func_process_app/public_custom_function/update' // 根据id修改功能
CUSTOM_DEL = '/func_process_app/public_custom_function/del' // 根据id删除功能
CUSTOM_CONFIG = '/func_process_app/public_custom_function/config' // 配置函数
CUSTOM_SIMPLE_RUN = '/func_process_app/public_custom_function/runSimpleTask' // 运行功能
RUN_PROCESS = '/func_process_app/public_custom_function/run_process' // 运行功能
ALL_CODE_MSG = '/func_process_app/public_error_code/getCodeMsg' // 获取所有返回码返回信息
CUSTOM_COMMIT = '/func_process_app/public_custom_function/commit' // 提交功能
CUSTOM_APPROVE = '/func_process_app/public_custom_function/approve' // 审批功能

// 编程规范
STANDARD_DATA = '/func_process_app/software_standard/get_software_standard_list' // 查询
STANDARD_ADD = '/func_process_app/software_standard/standard_add' // 新增数据
STANDARD_EDIT = '/func_process_app/software_standard/standard_edit' // 编辑数据
STANDARD_DEL = '/func_process_app/software_standard/standard_del' // 删除数据
UPLOAD_IMG = '/func_process_app/software_standard/fun_add_pic'// 上传图片

// 全局下拉框
GET_SELECT_LIST = '/platformorder_app/get_selected_list/' // 全局下拉框获取
QUERY_SELECT = '/platformorder_app/query_selected/' // 下拉框取枚举获取

// 评论
GET_COMMENTS = '/func_process_app/approve_comments/get_comment_data' // 获取当前数据评论信息
READ_COMMENT = '/func_process_app/approve_comments/read_comment' // 已读评论
ADD_COMMENT = '/func_process_app/approve_comments/add_comment' // 新增当前数据评论信息
IT_USER = '/func_process_app/approve_comments/get_it_user' // 获取it人员
IT_USERDESC = '/func_process_app/approve_comments/get_it_user_desc' // 获取it人员倒序
IT_TESTUSER = '/func_process_app/approve_comments/get_test_user' // 获取测试人员

// page
PAGE_LIST = '/func_process_app/public_pages/list' //获取页面列表  public/page_list_res
PAGE_PARAMS = '/func_process_app/public_pages/params_list_res'  //获取页面参数
PAGE_ADD = '/func_process_app/public_pages/add_page_list'  //添加页面数据
PAGE_DEL = '/func_process_app/public_pages/del_page_list'  //删除页面数据