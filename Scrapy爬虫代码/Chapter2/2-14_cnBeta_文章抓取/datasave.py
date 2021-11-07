import os
class DataSave:
    # 指定数据保存的文件路径
    def __init__(self,path):
        self.path = path

    def save(self,data):
        # 判断文件路径是否存在，如不存在则抛出错误
        if not os.path.exists(self.path):
            raise FileExistsError("文件路径不存在")
        # 将数据写入文件中,已追加形式写入文件
        with open(self.path,'a') as fp:
            print("开始写入数据")
            # 加上\n换行写入数据
            fp.write(str(data) + '\n')
        fp.close()

if __name__ == "__main__":
    test_data = 'this is a test,\n save it'
    save_path = 'C:\\Users\\gstar\\Desktop\\file.txt'
    ds = DataSave(save_path)
    ds.save(test_data)
