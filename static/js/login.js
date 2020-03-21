$(function(){
    var vertify_img=$("#vertify_img");
    vertify_img.click(function () {
        console.log("更新验证码")
        vertify_img.attr("src","/app/getvertifycode/"+Math.random());
        
    })

})