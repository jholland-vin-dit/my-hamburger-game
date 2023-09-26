def on_b_pressed():
    # mycomment
    my_burger.start_effect(effects.clouds, 5000)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    game.show_long_text(info.score(), DialogLayout.BOTTOM)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    scene.camera_shake(4, 200)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

my_burger: Sprite = None
info.set_score(0)
myplayer = sprites.create(img("""
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
    """),
    SpriteKind.player)
my_burger = sprites.create(img("""
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
    """),
    SpriteKind.food)
myplayer.set_stay_in_screen(True)
my_burger.set_position(25, 25)
my_burger.set_velocity(20, 20)
my_burger.set_stay_in_screen(False)
my_burger.set_bounce_on_wall(True)
controller.move_sprite(myplayer)
my_burger.set_stay_in_screen(True)