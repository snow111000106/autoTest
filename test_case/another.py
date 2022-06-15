try:
    self.assertEqual(self.driver.current_activity,
                     'com.xingjiabi.shengsheng.app.NavigationActivity', 'case filed2')
    print('case pass4')
except NoSuchElementException:
    if self.driver.find_element_by_id(
            'com.xingjiabi.shengsheng:id/md_content').text == '用户名或者密码输错啦，好好想想~ 错误码（a1208）':
        print('case pass5')
    elif find_toast("密码错误，请重新输入"):
        print('case pass6')
    else:
        print('NoSuchElementException')
except:
    print('error')