function get_list ()
{
    var result = "";
    $(".fav-video-list > li >a.title").each(function(){
        result += $(this).text() + '<br><a href="' + $(this).attr("href") + '" target=_blank >https:'+$(this).attr("href")+'</a><br>';
    });
    return result;
}
var html = "";
function main (){
    html += get_list();
    if($(".be-pager-next:visible").length == 0)
    {   
        document.write(html);
        return ;
    }else{
        $(".be-pager-next").click();
        setTimeout("main()",1000);
    }
}
main();