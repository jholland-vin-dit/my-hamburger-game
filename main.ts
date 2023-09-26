controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    // mycomment
    my_burger.startEffect(effects.clouds, 5000)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    game.showLongText(info.score(), DialogLayout.Bottom)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    scene.cameraShake(4, 200)
})
let my_burger: Sprite = null
// we're starting at 0
info.setScore(0)
let myplayer = sprites.create(img`
    . . . . . . . . . . 
    . . 2 2 2 2 2 2 2 . 
    . 2 . . . . . . . 2 
    . 2 . 2 2 . 2 2 . 2 
    . 2 . . . . . . . 2 
    . 2 . . . 2 . . . 2 
    . 2 . . . 2 . . . 2 
    . 2 . . . . . . . 2 
    . 2 . . 2 2 2 . . 2 
    . . 2 2 2 2 2 2 2 . 
    `, SpriteKind.Player)
my_burger = sprites.create(img`
    ...........ccccc66666...........
    ........ccc4444444444666........
    ......cc444444444bb4444466......
    .....cb4444bb4444b5b444444b.....
    ....eb4444b5b44444b44444444b....
    ...ebb44444b4444444444b444446...
    ..eb6bb444444444bb444b5b444446..
    ..e6bb5b44444444b5b444b44bb44e..
    .e66b4b4444444444b4444444b5b44e.
    .e6bb444444444444444444444bb44e.
    eb66b44444bb444444444444444444be
    eb66bb444b5b44444444bb44444444be
    fb666b444bb444444444b5b4444444bf
    fcb666b44444444444444bb444444bcf
    .fbb6666b44444444444444444444bf.
    .efbb66666bb4444444444444444bfe.
    .86fcbb66666bbb44444444444bcc688
    8772effcbbbbbbbbbbbbbbbbcfc22778
    87722222cccccccccccccccc22226678
    f866622222222222222222222276686f
    fef866677766667777776667777fffef
    fbff877768f86777777666776fffffbf
    fbeffeefffeff7766688effeeeefeb6f
    f6bfffeffeeeeeeeeeeeeefeeeeebb6e
    f66ddfffffeeeffeffeeeeeffeedb46e
    .c66ddd4effffffeeeeeffff4ddb46e.
    .fc6b4dddddddddddddddddddb444ee.
    ..ff6bb444444444444444444444ee..
    ....ffbbbb4444444444444444ee....
    ......ffebbbbbb44444444eee......
    .........fffffffcccccee.........
    ................................
    `, SpriteKind.Food)
myplayer.setStayInScreen(true)
my_burger.setPosition(25, 25)
my_burger.setVelocity(20, 20)
my_burger.setStayInScreen(false)
my_burger.setBounceOnWall(true)
controller.moveSprite(myplayer)
my_burger.setStayInScreen(true)
