console.log('js is loaded')


$('#more').on('click',function(){
  $('#hidden').slideDown( function(){
    $('#more').css({'display':'none'})
    $('#hide').css({'display':'initial'})

  })
})

$('#hide').on('click',function(){
  $('#hidden').slideUp( function(){
    $('#hide').css({'display':'none'})
    $('#more').css({'display':'initial'})

  })
})
