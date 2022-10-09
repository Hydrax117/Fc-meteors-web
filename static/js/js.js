console.log('js is loaded')



function one(n){
  $("#hidden"+n+" ").slideDown( function(){
    $("#more"+n+" ").css({'display':'none'})
    $("#hide"+n+' ').css({'display':'initial'})

  }) 
}

function two(n){
  $("#hide"+n+" ").on('click',function(){
    $('#hidden'+n+' ').slideUp( function(){
      $('#hide'+n+' ').css({'display':'none'})
      $('#more'+n+' ').css({'display':'initial'})
  
    })
  })
  
}
// $('#more').on('click',function(){
//   $('#hidden').slideDown( function(){
//     $('#more').css({'display':'none'})
//     $('#hide').css({'display':'initial'})

//   })
// })

// $('#hide').on('click',function(){
//   $('#hidden').slideUp( function(){
//     $('#hide').css({'display':'none'})
//     $('#more').css({'display':'initial'})

//   })
// })

$('#more1').on('click',function(){
  $('#hidden1').slideDown( function(){
    $('#more1').css({'display':'none'})
    $('#hide1').css({'display':'initial'})

  })
})

$('#hide1').on('click',function(){
  $('#hidden1').slideUp( function(){
    $('#hide1').css({'display':'none'})
    $('#more1').css({'display':'initial'})

  })
})
