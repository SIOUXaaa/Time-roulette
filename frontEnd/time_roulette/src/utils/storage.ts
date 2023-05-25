/* 存储数据 */
export const setItem = (key:string, value:any) => {
    // 将数组、对象类型的数据转换为 JSON 格式字符串进行存储
    if (typeof value === "object") {
        value = JSON.stringify(value);
    }
    window.localStorage.setItem(key, value);
};

/* 获取数据 */
export const getItem = (key:any) => {
    const data = window.localStorage.getItem(key);
    try {
        if(data)
            return JSON.parse(data);
    } catch (err) {
        return data;
    }
};

/* 删除数据 */
export const removeItem = (key:any) => {
    window.localStorage.removeItem(key);
};