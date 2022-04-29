function openForm() {
    let inputVal = document.getElementById("email").value;
    
}
function closeForm() {
    document.getElementById("popupForm").style.display = "none";
}

function add() {
    let firstName = document.getElementById("userFirstName").value;
    let lastName = document.getElementById("userLastName").value;
    let destCity = document.getElementById("destinationCity").value;
    let email = document.getElementById("email").value;
    let pass = document.getElementById("password").value;
    var url = window.location.href;
    var len = url.length;
    url = url.slice(0, len-6);    
    window.location = (url);
    url =  url + 'create?first='+firstName+'&last='+lastName+'&destCity='+destCity+'&email='+email+'&pass='+pass;
    window.location = (url);
    console.log("Done with ajax");
};

function deleteOne() {
    let email = document.getElementById("deleteEmail").value;
    var url = window.location.href;
    var len = url.length;
    var list = url.split("/");
    target = 0;
    // for (var i = 0; i < list.length; i++){
        // alert(list[i]);
    // }
    url = list[0] + "//" + list[2];
    //url = 'My name is '.concat(name, ', and I\'m from ', country);


    window.location = (url);
    url =  url + '/delete?e='+email;
    window.location = (url);
    // $.ajax({
    //     type: 'POST',
    //     url: '/delete?e='+email,
    //     contentType: 'application/jason;charset=UTF-8',
    //     success: function (res) {
    //         console.log(res.response);
    //         location.reload();
    //     },
    //     error: function() {
    //         console.log('Error');
    //     }
    // });
};

function update() {
    let firstName = document.getElementById("userFirstNameUpdate").value;
    let lastName = document.getElementById("userLastNameUpdate").value;
    let destCity = document.getElementById("destinationCityUpdate").value;
    let email = document.getElementById("emailUpdate").value;
    let pass = document.getElementById("passwordUpdate").value;
    var url = window.location.href;
    var len = url.length;
    var list = url.split("/");
    target = 0;
    // for (var i = 0; i < list.length; i++){
        // alert(list[i]);
    // }
    url = list[0] + "//" + list[2];
    //url = 'My name is '.concat(name, ', and I\'m from ', country);


    window.location = (url);
    url =  url + '/update?first='+firstName+'&last='+lastName+'&destCity='+destCity+'&email='+email+'&pass='+pass;
    window.location = (url);
};

function search() {
    let country = document.getElementById("searchCountry").value;
    $.ajax({
        type:'POST',
        url: '/search?c='+country,
        success: function (res) {
            console.log(res.response);
        },
        error: function() {
            console.log('Error');
        }
    });
};

function loginRedirect() {
    url = (window.location.href + 'login'); 
    window.location = url;
};

function signUpRedirect() {
    url = (window.location.href + 'signup');
    window.location = url; 
};

function userProfileRedirect() {
    url = (window.location.href + 'userprofile');
    window.location = url; 
};

function moreDetails() {
    url = (window.location.href + 'moreDetail'); 
    window.location = url;
};

function about() {
    window.location = 'https://github-dev.cs.illinois.edu/sp22-cs411/sp22-cs411-team101-abduFormedTeam';
};

function abdu() {
    window.location = 'https://cs.illinois.edu/about/people/faculty/alawini';
};

function showDestinationCity() {
    var url = window.location.href;
    var list = url.split("/");
    
    url = list[0] + "//" + list[2];
    window.location = (url);

    url =  url + '/showDestinationCity';
    window.location = (url);
};

function createRating() {
    numRating = document.getElementById("numberRating").value;
    review = document.getElementById("review").value;

    var url = window.location.href;
    var list = url.split("/");
    
    url = list[0] + "//" + list[2];
    window.location = (url);
    alert(url);
    url =  url + '/createReview?numRating='+numRating+'&review='+review;
    alert(url);
    window.location = (url);
}

// $(document).ready(function () {
//     // example: https://getbootstrap.com/docs/4.2/components/modal/
//     // show modal

    

//     // $('#task-modal').on('show.bs.modal', function (event) {
//     //     const button = $(event.relatedTarget) // Button that triggered the modal
//     //     const taskID = button.data('source') // Extract info from data-* attributes
//     //     const content = button.data('content') // Extract info from data-* attributes

//     //     const modal = $(this)
//     //     if (taskID === 'New Task') {
//     //         modal.find('.modal-title').text(taskID)
//     //         $('#task-form-display').removeAttr('taskID')
//     //     } else {
//     //         modal.find('.modal-title').text('Edit Task ' + taskID)
//     //         $('#task-form-display').attr('taskID', taskID)
//     //     }

//     //     if (content) {
//     //         modal.find('.form-control').val(content);
//     //     } else {
//     //         modal.find('.form-control').val('');
//     //     }
//     // })


//     // $('#submit-task').click(function () {
//     //     const tID = $('#task-form-display').attr('taskID');
//     //     console.log($('#task-modal').find('.form-control').val())
//     //     $.ajax({
//     //         type: 'POST',
//     //         url: tID ? '/edit/' + tID : '/create',
//     //         contentType: 'application/json;charset=UTF-8',
//     //         data: JSON.stringify({
//     //             'description': $('#task-modal').find('.form-control').val()
//     //         }),
//     //         success: function (res) {
//     //             console.log(res.response)
//     //             location.reload();
//     //         },
//     //         error: function () {
//     //             console.log('Error');
//     //         }
//     //     });
//     // });

//     // $('.remove').click(function () {
//     //     const remove = $(this)
//     //     $.ajax({
//     //         type: 'POST',
//     //         url: '/delete/' + remove.data('source'),
//     //         success: function (res) {
//     //             console.log(res.response)
//     //             location.reload();
//     //         },
//     //         error: function () {
//     //             console.log('Error');
//     //         }
//     //     });
//     // });

//     // $('.state').click(function () {
//     //     const state = $(this)
//     //     const tID = state.data('source')
//     //     const new_state
//     //     if (state.text() === "In Progress") {
//     //         new_state = "Complete"
//     //     } else if (state.text() === "Complete") {
//     //         new_state = "Todo"
//     //     } else if (state.text() === "Todo") {
//     //         new_state = "In Progress"
//     //     }

//     //     $.ajax({
//     //         type: 'POST',
//     //         url: '/edit/' + tID,
//     //         contentType: 'application/json;charset=UTF-8',
//     //         data: JSON.stringify({
//     //             'status': new_state
//     //         }),
//     //         success: function (res) {
//     //             console.log(res)
//     //             location.reload();
//     //         },
//     //         error: function () {
//     //             console.log('Error');
//     //         }
//     //     });
//     // });

// });