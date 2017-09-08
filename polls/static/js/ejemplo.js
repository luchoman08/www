$(document).ready(function(){
    
    $('.panel > .panel-body > .alert > .close').click(
        function() { 
            $(this).parents(".producto").hide("slow");
        }
    );
    $('#search').change(
        
        function (){
            $('.producto').hide();
            $('.producto > .panel> .panel-heading > .panel-title:contains('+$(this).val() +')').parents(".producto").show();
            
            
        }
    );
   
    });