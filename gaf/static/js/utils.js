'use strict';

/* Utils */

function setQueryStringPage(queryString, page){
	return queryString.split("page")[0] + "page=" + page.toString();
}

function notifyResponse(data, headersGetter, status){
    var json_response = parseResponse(data, headersGetter, status);
    if( status == 200) {
        notifySuccess(json_response.message);
        return json_response;
    } else {
        notifyError(json_response.message);
        return false;
    }
}

function parseResponse(data, headersGetter, status){
    if( status == 401 || status == 405) {
        window.location.href = '/';
    }
    return angular.fromJson(data);
}

function notifySuccess(message){
	$.bootstrapGrowl(message, {type: 'success', delay: 2000});
}

function notifyError(message){
	$.bootstrapGrowl(message, {type: 'danger', delay: 2000});
}

function validateImageUpload(file){
    if( ['jpg', 'gif', 'png', 'jpeg'].indexOf(file.getExtension()) == -1 ) {
        notifyError('Please upload a PNG, JPG or GIF');
        return false;
    }
    if( file.file.size > 2000000) {
        notifyError('Please upload a file smaller than 2 MB');
        return false;
    }
    return true;
}