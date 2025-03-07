from manim import *

class SimpleRadarBasics(Scene):
    """
    Version simplifiée de la scène RadarBasics pour éviter les problèmes de LaTeX
    """
    def construct(self):
        # Titre
        title = Text("Principes de la télédétection radar", font_size=42)
        subtitle = Text("Mesure de l'humidité du sol", font_size=32, color=BLUE)
        subtitle.next_to(title, DOWN)
        
        # Animation du titre
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(1)
        
        # Déplacer le titre vers le haut
        self.play(
            title.animate.scale(0.6).to_edge(UP, buff=0.2),
            subtitle.animate.scale(0.6).next_to(title, DOWN, buff=0.1),
            run_time=1
        )
        
        # Principe de base du radar
        radar_principle = Text("Comment fonctionne un radar?", font_size=32, color=YELLOW)
        radar_principle.next_to(subtitle, DOWN, buff=0.7)
        
        # Animation du principe radar
        self.play(Write(radar_principle), run_time=1)
        
        # Créer un schéma simple du principe radar
        # Créer la surface et le radar
        radar = Circle(radius=0.3, color=WHITE)
        radar.set_fill(GRAY, opacity=0.5)
        radar.move_to(UP * 2 + LEFT * 4)
        
        radar_dish = Arc(radius=0.5, angle=PI/2, color=WHITE)
        radar_dish.next_to(radar, RIGHT, buff=-0.5)
        
        # Surface du sol
        ground = Line(LEFT * 7, RIGHT * 7, color=BROWN)
        ground.move_to(DOWN * 2)
        
        # Onde radar
        radar_wave_out = DashedLine(radar.get_center(), ground.point_from_proportion(0.7), color=YELLOW)
        radar_wave_back = DashedLine(ground.point_from_proportion(0.7), radar.get_center(), color=RED)
        
        # Ajouter des étiquettes
        emitted_label = Text("Signal émis", font_size=20, color=YELLOW)
        emitted_label.next_to(radar_wave_out.get_center(), UP+RIGHT, buff=0.3)
        
        reflected_label = Text("Signal rétrodiffusé", font_size=20, color=RED)
        reflected_label.next_to(radar_wave_back.get_center(), UP+LEFT, buff=0.3)
        
        # Animation du schéma radar
        self.play(
            Create(radar),
            Create(radar_dish),
            Create(ground),
            run_time=1.5
        )
        
        # Visualiser l'émission de l'onde
        self.play(Create(radar_wave_out), run_time=1)
        self.play(Write(emitted_label), run_time=0.5)
        self.wait(0.5)
        
        # Visualiser la réflexion de l'onde
        self.play(Create(radar_wave_back), run_time=1)
        self.play(Write(reflected_label), run_time=0.5)
        self.wait(1)
        
        # Introduction au coefficient de rétrodiffusion
        backscatter_title = Text("Coefficient de rétrodiffusion (σ°)", font_size=28, color=GREEN)
        backscatter_title.to_edge(RIGHT).shift(UP * 1.5 + LEFT * 3)
        
        # Utilisation de Text au lieu de BulletedList (qui utilise LaTeX)
        bullet1 = Text("• Mesure l'intensité du signal retourné vers le capteur", font_size=22)
        bullet2 = Text("• Exprimé en décibels (dB)", font_size=22)
        bullet3 = Text("• Dépend des propriétés de la surface", font_size=22)
        
        bullets = VGroup(bullet1, bullet2, bullet3).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        bullets.next_to(backscatter_title, DOWN, aligned_edge=LEFT, buff=0.3)
        
        # Animation de la définition du coefficient de rétrodiffusion
        self.play(Write(backscatter_title), run_time=1)
        self.play(Write(bullets), run_time=2)
        self.wait(1.5)
        
        # Formule du coefficient de rétrodiffusion (simplifiée)
        formula = Text("σ° ∝ Ks · εr", font_size=32)
        formula.next_to(bullets, DOWN, buff=0.5)
        
        formula_explanation = VGroup(
            Text("Où:", font_size=22),
            Text("Ks = facteur de rugosité", font_size=22),
            Text("εr = permittivité relative (liée à l'humidité)", font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT)
        formula_explanation.next_to(formula, DOWN, buff=0.3)
        
        # Animation de la formule
        self.play(Write(formula), run_time=1.5)
        self.play(Write(formula_explanation), run_time=2)
        self.wait(2)
        
        # Conclusion
        conclusion = Text(
            "La télédétection radar permet de mesurer l'humidité du sol\n"
            "en utilisant les propriétés de rétrodiffusion des surfaces.",
            font_size=28,
            t2c={"humidité du sol": YELLOW, "propriétés de rétrodiffusion": GREEN}
        )
        conclusion.to_edge(DOWN, buff=0.5)
        
        self.play(Write(conclusion), run_time=2)
        self.wait(2)


class SimpleBrightnessTemperature(Scene):
    """
    Version simplifiée de l'animation sur la température de brillance
    sans les éléments qui causent des erreurs
    """
    def construct(self):
        # Configuration de la scène avec fond noir
        self.camera.background_color = BLACK
        
        # Titre avec style amélioré
        title = Text("Évolution de la Température de Brillance", font_size=48, color=WHITE)
        subtitle = Text("Pendant le gel de l'eau salée en Arctique", font_size=36, color=BLUE_B)
        
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        
        self.play(Write(title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP*0.2), run_time=1)
        self.wait(1)
        
        self.play(
            title_group.animate.scale(0.7).to_edge(UP, buff=0.5),
            run_time=1
        )
        
        # Configuration des axes avec meilleur positionnement
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.2, 0.2],
            axis_config={
                "include_tip": True,
                "include_numbers": True,
                "font_size": 24,
                "stroke_width": 2,
                "color": WHITE,
            },
            x_length=9,
            y_length=5,
        ).shift(DOWN*0.5)
        
        # Étiquettes d'axes plus lisibles
        x_label = Text("Temps (jours)", font_size=24, color=WHITE)
        x_label.next_to(axes, DOWN)
        
        y_label = Text("Valeur normalisée", font_size=24, color=WHITE)
        y_label.next_to(axes, LEFT).rotate(PI/2)
        
        # Définition des fonctions pour les courbes
        def physical_temperature(x):
            # Température physique avec légère diminution pendant la transition
            if x < 3:
                return 1.0  # Eau à température initiale
            elif x < 6:
                return 1.0 - 0.1 * (x - 3) / 3  # Légère baisse pendant la transition
            else:
                return 0.9  # Eau gelée (légèrement plus froide)
        
        def emissivity(x):
            # Émissivité qui change pendant la transition eau-glace
            # Valeurs basées sur des mesures scientifiques
            if x < 3:
                return 0.55  # Émissivité de l'eau de mer (19-37 GHz)
            elif x < 6:
                return 0.55 + (0.92 - 0.55) * (x - 3) / 3  # Transition progressive
            else:
                return 0.92  # Émissivité de la nouvelle glace de mer
        
        def brightness_temperature(x):
            # Température de brillance = émissivité * température physique
            return emissivity(x) * physical_temperature(x)
        
        # Création des courbes avec épaisseur et couleurs distinctes
        temp_phys_curve = axes.plot(
            physical_temperature,
            x_range=[0, 10],
            color=BLUE_C,
            stroke_width=4,
        )
        
        emissivity_curve = axes.plot(
            emissivity,
            x_range=[0, 10],
            color=GREEN_D,
            stroke_width=4,
        )
        
        tb_curve = axes.plot(
            brightness_temperature,
            x_range=[0, 10],
            color=RED_C,
            stroke_width=4,
        )
        
        # Placement plus clair des étiquettes de courbes
        temp_phys_label = Text("Température physique", font_size=28, color=BLUE_C)
        temp_phys_label.to_edge(RIGHT).shift(UP*1.5 + LEFT*3)
        
        emissivity_label = Text("Émissivité (ε)", font_size=28, color=GREEN_D)
        emissivity_label.to_edge(RIGHT).shift(UP*0.5 + LEFT*5)
        
        tb_label = Text("Température de brillance (Tᴮ)", font_size=28, color=RED_C)
        tb_label.to_edge(RIGHT).shift(DOWN*0.5 + LEFT*2.5)
        
        # Animation progressive
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=1.5)
        self.wait(0.5)
        
        # Visualisation de l'océan et de la formation de glace
        ocean = Rectangle(width=9, height=1.2, fill_opacity=0.8, fill_color="#0C2D48", stroke_color=BLUE_E)
        ocean.next_to(axes, DOWN, buff=1.75)
        
        ocean_label = Text("Océan Arctique", font_size=28, color=BLUE_E)
        ocean_label.next_to(ocean, UP, buff=0.2)
        
        self.play(
            FadeIn(ocean),
            Write(ocean_label),
            run_time=1
        )
        
        # Animation de la courbe de température physique
        self.play(
            Create(temp_phys_curve),
            Write(temp_phys_label),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Animation de la courbe d'émissivité
        self.play(
            Create(emissivity_curve),
            Write(emissivity_label),
            run_time=1.5
        )
        
        # Animation de la courbe de température de brillance
        self.play(
            Create(tb_curve),
            Write(tb_label),
            run_time=2
        )
        self.wait(1)
        
        # Visualisation de la formation de glace avec transition claire
        ice_formation = Rectangle(width=0, height=1.2, fill_opacity=0.9, fill_color="#B3E5FC", stroke_width=0)
        ice_formation.align_to(ocean, DOWN+LEFT)
        
        self.play(
            GrowFromPoint(ice_formation, ice_formation.get_center(), rate_func=rate_functions.linear),
            ice_formation.animate.stretch_to_fit_width(9),
            run_time=3
        )
        
        # Formules dans un cadre
        formula_box = Rectangle(width=6, height=2.5, fill_opacity=0.8, fill_color=BLACK, stroke_color=YELLOW, stroke_width=3)
        formula_box.to_edge(LEFT, buff=0.5).shift(UP*2.5)
        
        formula_title = Text("Équation fondamentale", font_size=30, color=YELLOW)
        formula_title.next_to(formula_box.get_top(), DOWN, buff=0.2)
        
        formula = Text("Tᴮ(θ, ν) = ε(θ, ν) · Tphys", font_size=30)
        formula.next_to(formula_title, DOWN, buff=0.3)
        
        self.play(
            FadeIn(formula_box),
            Write(formula_title),
            run_time=1
        )
        
        self.play(
            Write(formula),
            run_time=1.5
        )
        
        # Message final
        final_message = Text(
            "La température de brillance augmente significativement\n"
            "en raison de l'augmentation de l'émissivité lors\n"
            "de la formation de glace.",
            font_size=32,
            color=YELLOW
        )
        final_message.to_edge(DOWN, buff=0.8)
        
        self.play(
            Write(final_message),
            run_time=2
        )
        self.wait(3)
