from manim import *

class BrightnessTemperatureEvolutionImproved(Scene):
    """
    Version améliorée de l'animation sur l'évolution de la température de brillance
    avec une meilleure disposition des éléments et clarté visuelle
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
        x_label = axes.get_x_axis_label(MathTex("\\text{Temps (jours)}", color=WHITE), edge=DOWN, direction=DOWN)
        y_label = axes.get_y_axis_label(MathTex("\\text{Valeur normalisée}", color=WHITE), edge=LEFT, direction=LEFT).shift(LEFT*0.5)
        
        axes_labels = VGroup(x_label, y_label)
        
        # Définition scientifique des fonctions pour les courbes avec séparation claire
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
        
        # Animation progressive avec pauses pour meilleure lisibilité
        self.play(Create(axes), Write(axes_labels), run_time=1.5)
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
        
        # Textes d'explication scientifique avec positionnement clair
        phase_water = Text("Phase liquide: émissivité basse", font_size=22, color=WHITE)
        phase_water.next_to(ocean, DOWN, buff=0.2).align_to(ocean, LEFT).shift(RIGHT*1.5)
        
        phase_transition = Text("Transition: formation de glace", font_size=22, color=WHITE)
        phase_transition.next_to(phase_water, RIGHT, buff=1)
        
        phase_ice = Text("Phase solide: émissivité élevée", font_size=22, color=WHITE)
        phase_ice.next_to(phase_transition, RIGHT, buff=1)
        
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
        
        # Ajout du texte de la phase liquide
        self.play(Write(phase_water), run_time=1)
        self.wait(0.5)
        
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
            ice_formation.animate.stretch_to_fit_width(3),
            Write(phase_transition),
            run_time=2
        )
        self.wait(0.3)
        
        self.play(
            ice_formation.animate.stretch_to_fit_width(9),
            Write(phase_ice),
            run_time=3
        )
        self.wait(1)
        
        # Formules scientifiques dans un cadre bien délimité et positionné clairement
        formula_box = Rectangle(width=6, height=3, fill_opacity=0.8, fill_color=BLACK, stroke_color=YELLOW, stroke_width=3)
        formula_box.to_edge(LEFT, buff=0.5).shift(UP*2.5)
        
        formula_title = Text("Équations fondamentales", font_size=30, color=YELLOW)
        formula_title.next_to(formula_box.get_top(), DOWN, buff=0.2)
        
        tb_formula = MathTex(
            r"T_B(\theta, \nu) = \varepsilon(\theta, \nu) \cdot T_{phys}",
            font_size=30
        )
        tb_formula.next_to(formula_title, DOWN, buff=0.3)
        
        formula_explanation1 = MathTex(r"T_B &: \text{Température de brillance}", font_size=24)
        formula_explanation2 = MathTex(r"\varepsilon &: \text{Émissivité (dépend de}~\theta, \nu\text{)}", font_size=24)
        formula_explanation3 = MathTex(r"T_{phys} &: \text{Température physique}", font_size=24)
        
        explanations = VGroup(formula_explanation1, formula_explanation2, formula_explanation3)
        explanations.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explanations.next_to(tb_formula, DOWN, buff=0.4)
        
        self.play(
            FadeIn(formula_box),
            Write(formula_title),
            run_time=1
        )
        
        self.play(
            Write(tb_formula),
            run_time=1
        )
        
        self.play(
            Write(explanations),
            run_time=1.5
        )
        self.wait(1)
        
        # Boîte d'implications scientifiques bien positionnée
        implications_box = Rectangle(width=6, height=3, fill_opacity=0.8, fill_color=BLACK, stroke_color=BLUE, stroke_width=3)
        implications_box.to_edge(RIGHT, buff=0.5).shift(UP*2.5)
        
        implications_title = Text("Conséquences", font_size=30, color=BLUE)
        implications_title.next_to(implications_box.get_top(), DOWN, buff=0.2)
        
        implications_bullet1 = MathTex(r"\bullet~", r"\text{Augmentation de}~T_B~\text{malgré une}~T_{phys}~\text{constante}", font_size=20)
        implications_bullet2 = MathTex(r"\bullet~", r"\text{Émissivité:}~0.45\text{-}0.65~(\text{eau})~\rightarrow~0.92~(\text{glace})", font_size=20)
        implications_bullet3 = MathTex(r"\bullet~", r"\text{Permettra la cartographie de l'étendue de glace}", font_size=20)
        
        implications_bullets = VGroup(implications_bullet1, implications_bullet2, implications_bullet3)
        implications_bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        implications_bullets.next_to(implications_title, DOWN, buff=0.3)
        
        self.play(
            FadeIn(implications_box),
            Write(implications_title),
            run_time=1
        )
        
        self.play(
            Write(implications_bullets),
            run_time=2
        )
        self.wait(1)
        
        # Message final distinct et bien positionné
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
