// api
APPROVE_PERSON = '/public_user_info/is_approve_person' // 用户名
// 参数
PARAM_PAGE = '/public_params/page' // 参数列表查询
PARAM_CHILD_PAGE = '/public_params/page_child' // 参数列表包含子参数查询
PARAM_LIST = '/public_params/paramlist' // 参数列表滚动查询
PARAM_CHILD = '/public_params/childParam' // 查询子参数
PARAM_BY_IDLIST = '/public_params/getByIdList' // 根据id列表查询参数
PARAM_ADD = '/public_params/add' // 新增参数
PARAM_EDIT = '/public_params/update' // 根据id修改参数
PARAM_DEL = '/public_params/del' // 根据id删除参数
PARAM_COMMIT = '/public_params/commit' // 提交参数
PARAM_APPROVE = '/public_params/approve' // 审批参数

// 返回码
ERROR_CODE_LIST = '/public_error_code/list' // 返回码列表滚动查询
ERROR_CODE_ADD = '/public_error_code/add' // 新增返回码
ERROR_CODE_EDIT = '/public_error_code/update' // 根据id修改返回码
ERROR_CODE_DEL = '/public_error_code/del' // 根据id删除返回码
ERROR_CODE_BYTASKID = '/public_custom_function/getErrorCode' // 查询流程返回码

// 类名
CLASS_ADD = '/public_class/add' // 新增类
CLASS_EDIT = '/public_class/edit' // 修改类
CLASS_DEL = '/public_class/del' // 删除类
CLASS_LIST = '/public_class/list' // 类列表

// 函数
FUNCTION_LIST = '/public_function/list' // 函数列表查询
FUNCTION_SIMPLE_LIST = '/public_function/simpleList' // 函数列表查询
FUNCTION_ADD = '/public_function/add' // 新增函数
FUNCTION_EDIT = '/public_function/update' // 根据id修改函数
FUNCTION_DEL = '/public_function/del' // 根据id删除函数
FUNCTION_RUN = '/public_function/runFunction' // 函数调试
FUNCTION_SHOW = '/public_function/showFunction' // 展示函数体
FUNCTION_COMMIT = '/public_function/commit' // 提交函数
FUNCTION_APPROVE = '/public_function/approve' // 审批函数
FUNCTION_PUBLISH = '/public_function/publish' // 发布函数
FUNCTION_ADD_AUTO_TEST = '/public_function/add_auto_test' // 加入自动化测试

// 函数参数
FUNC_PARAM_BYFUNID = '/fun_param/getByFunId' // 根据函数id查询参数和返回值
CUSTOM_PARAM_BY_FUNCLIST = '/fun_param/getByFunListId' // 功能配置根据函数id查询参数和返回值
// 函数组合
CUSTOM_LIST = '/public_custom_function/list' // 功能列表查询
CUSTOM_ADD = '/public_custom_function/add' // 新增功能
CUSTOM_EDIT = '/public_custom_function/update' // 根据id修改功能
CUSTOM_DEL = '/public_custom_function/del' // 根据id删除功能
CUSTOM_CONFIG = '/public_custom_function/config' // 配置函数
CUSTOM_SIMPLE_RUN = '/public_custom_function/runSimpleTask' // 运行功能
RUN_PROCESS = '/public_custom_function/run_process' // 运行功能
ALL_CODE_MSG = '/public_error_code/getCodeMsg' // 获取所有返回码返回信息
CUSTOM_COMMIT = '/public_custom_function/commit' // 提交功能
CUSTOM_APPROVE = '/public_custom_function/approve' // 审批功能

// 编程规范
STANDARD_DATA = '/software_standard/get_software_standard_list' // 查询
STANDARD_ADD = '/software_standard/standard_add' // 新增数据
STANDARD_EDIT = '/software_standard/standard_edit' // 编辑数据
STANDARD_DEL = '/software_standard/standard_del' // 删除数据
UPLOAD_IMG = '/software_standard/fun_add_pic'// 上传图片

// 全局下拉框
GET_SELECT_LIST = '/get_selected_list/' // 全局下拉框获取
QUERY_SELECT = '/query_selected/' // 下拉框取枚举获取
GET_ENUM_OPTIONS = '/global_enum/get_enum_options/'//根据参数名获取枚举下拉框数据
VIEW_PAGE = '/public_custom_function/viewPage'//预览页面

// 评论
GET_COMMENTS = '/approve_comments/get_comment_data' // 获取当前数据评论信息
READ_COMMENT = '/approve_comments/read_comment' // 已读评论
ADD_COMMENT = '/approve_comments/add_comment' // 新增当前数据评论信息
IT_USER = '/approve_comments/get_it_user' // 获取it人员


//page
PAGE_LIST = '/public_pages/list' //获取页面列表  public/page_list_res
PAGE_PARAMS = '/public_pages/params_list_res'  //获取页面参数
PAGE_ADD = '/public_pages/add_page_list'  //添加页面数据
PAGE_DEL = '/public_pages/del_page_list'  //删除页面数据
