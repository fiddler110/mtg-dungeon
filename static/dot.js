$(document).ready(function(){
    //  here I asign the event dynamically, not needed for 'body' as such tag should always be present,
    //  but something you should look into
    //  see also: http://api.jquery.com/on/

    $(document).on('click', function(e) {
        if (typeof browser === "undefined") {
            var browser = chrome;
        }
        mouseX = e.pageX;
        mouseY = e.pageY
        //  simply press F12 to look at your browsers console and see the results
        console.log('Mouse Position:\t' + mouseX + '|' + mouseY);
        //  no need in JS to write var for every variable declartion,
        //  just seperate with a comma
        var color = '#555555',
            size = '10px';   //  changed size to 5px from 1 just to make it easier to see what's going on for you
        //  No need to use $("body") since this event takes place on the body tag
        //  $(this), in an event, always equals the selector the event is tied to
        $(this).append(
            //  making an element with jquery is simple
            //  no need to insert whole tag, all you need is tag name and a closer
            //  like so
            $('<div />')
                //  easily tie all css together
                .css({
                    //  also, in jquery CSS, any css variable with a '-' 
                    //  can be renamed when assigning
                    //  simply remove the '-' and capitilize the first letter of the second word
                    //  like so, here in 'background-color'
                    backgroundColor: color,
                    height: size,
                    left: mouseX + 'px',
                    position: 'absolute',
                    top: mouseY + 'px',
                    width: size
                })
        );
    })
});