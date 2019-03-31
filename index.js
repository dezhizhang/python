function ajax(config) {
    var xhr = new XMLHttpRequest();
    xhr.open(config.type, config.url, true);
    xhr.send(config.data);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            if (config.dataType == 'json') {
                console.log(JSON.parse(xhr.responseText));
            }
            else {
                return xhr.responseText;
            }
        }
    };
}
var json = ajax({
    type: 'get',
    url: 'https://cnodejs.org/api/v1/topics',
    data: '1',
    dataType: 'json'
});
