$(document).ready(function() {

    var tasks = {};
    $('.task').each(function(i) {
      tasks[$(this).attr('id')] = {"object": $(this), "checked": false};
    });
    var counter_checked = 0;

    function get_tasks_id(checked) {
        let tasks_id = [];
        for (let key in tasks) {
            if (checked == tasks[key]["checked"]) {
                tasks_id.push(Number(key));
            }
        }
        return tasks_id;
    }

    function tasks_delete(tasks_id) {
        tasks_id.forEach(task_id => {
            $("#"+task_id).remove();
            delete tasks[task_id.toString()]
        });
        $(".toolbar").css({"display": "none"});
        if (Object.keys(tasks).length == 0) {
            $(".tasks").append('<div class="task_empty">Пока что тут тишина, создайте задачу...</div>')
        }
        counter_checked = 0;
    }


    $(".task_mark").click(function(){
        var parent_id = $(this).parent().attr('id');
        if (parent_id in tasks) {
            if (tasks[parent_id]["checked"]) {
                $("#"+parent_id+" .task_mark").css({"background": "white"});
                $("#"+parent_id+" .task_mark").removeClass("opacity_enable");
                $("#"+parent_id).css({"background": "#eaeaea"});
                tasks[parent_id]["checked"] = false;
                counter_checked -= 1;
            }
            else {
                $("#"+parent_id+" .task_mark").css({"background": "black"});
                $("#"+parent_id+" .task_mark").addClass("opacity_enable");
                $("#"+parent_id).css({"background": "#717171"});
                tasks[parent_id]["checked"] = true;
                counter_checked += 1;
            }
            if (counter_checked > 0) {
                $(".toolbar").css({"display": "block"});
                if (counter_checked == 1) {
                    $(".edit_task").css({"display": "flex"});
                }
                else {
                    $(".edit_task").css({"display": "none"});
                }
            }
            else {
                $(".toolbar").css({"display": "none"});
            }
        }
    });

    $('.delete_tasks').click(function() {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "delete_tasks/");
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        tasks_id_arr = get_tasks_id(true);
        var data = {
            tasks_id: tasks_id_arr
        };
        xhr.send(JSON.stringify(data));

        xhr.onload = function(res) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                tasks_delete(tasks_id_arr);
            } else {
              console.error("ERROR");
            }
          }
        };
    });

    $(".edit_task").click(function() {
        window.location.href = 'edit_task/?task_id='+get_tasks_id(true)[0];
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

});