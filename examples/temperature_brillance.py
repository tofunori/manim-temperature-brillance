from manim import *

class EvolutionTemperatureBrillance(Scene):
    def construct(self):
        # Titre
        title = Text("Évolution de Tᴮ lors du gel de l'eau salée", font_size=40)
        self.play(Write(title))
        self.wait()
        self.play(title.animate.scale(0.7).to_edge(UP))
        
        # Configuration des axes pour le graphique
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.5, 0.5],
            axis_config={"include_tip": False, "numbers_to_exclude": []}
        )
        
        x_label = axes.get_x_axis_label("Temps")
        y_label = axes.get_y_axis_label("Valeur")
        
        # Courbe de la température physique (constante)
        temp_phys_curve = axes.plot(
            lambda x: 1,
            color=BLUE
        )
        temp_phys_label = Text("Température physique", font_size=20, color=BLUE).next_to(temp_phys_curve, UP)
        
        # Courbe de l'émissivité
        def emissivity(x):
            if x < 3:
                return 0.55  # Eau de mer
            elif x < 6:
                return 0.55 + (0.92 - 0.55) * (x - 3) / 3  # Transition
            else:
                return 0.92  # Glace
        
        emissivity_curve = axes.plot(
            emissivity,
            x_range=[0, 10],
            color=GREEN
        )
        emissivity_label = Text("Émissivité", font_size=20, color=GREEN).next_to(emissivity_curve.get_end(), RIGHT)
        
        # Courbe de la température de brillance (Tᴮ)
        def brightness_temp(x):
            return emissivity(x) * 1  # Tᴮ = émissivité * température physique
        
        tb_curve = axes.plot(
            brightness_temp,
            x_range=[0, 10],
            color=RED
        )
        tb_label = Text("Température de brillance (Tᴮ)", font_size=20, color=RED).next_to(tb_curve.get_end(), RIGHT)
        
        # Animation du système physique
        ocean = Rectangle(width=6, height=2, fill_opacity=0.8, color=BLUE_E)
        ocean.move_to(DOWN * 3)
        ocean_label = Text("Océan arctique", font_size=25).next_to(ocean, UP)
        
        # Affichage des valeurs
        emissivity_value_water = MathTex(r"\text{Émissivité eau} \approx 0.45-0.65", color=GREEN).to_edge(LEFT).shift(DOWN)
        emissivity_value_ice = MathTex(r"\text{Émissivité glace} \approx 0.92", color=GREEN).next_to(emissivity_value_water, DOWN)
        
        # Ajout des éléments à la scène
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(ocean), Write(ocean_label))
        self.play(Write(emissivity_value_water), Write(emissivity_value_ice))
        
        # Animation des courbes
        self.play(Create(temp_phys_curve), Write(temp_phys_label))
        self.wait()
        
        self.play(Create(emissivity_curve), Write(emissivity_label))
        self.wait()
        
        self.play(Create(tb_curve), Write(tb_label))
        self.wait()
        
        # Animation de la transition eau-glace
        ice_formation = Rectangle(width=0, height=2, fill_opacity=0.7, color=WHITE)
        ice_formation.align_to(ocean, DOWN+LEFT)
        
        self.play(
            GrowFromPoint(ice_formation, ice_formation.get_center(), rate_func=rate_functions.linear),
            ice_formation.animate.stretch_to_fit_width(6),
            run_time=5
        )
        
        # Conclusion
        conclusion = Text(
            "La température de brillance Tᴮ augmente significativement\n"
            "malgré une température constante, en raison de\n"
            "l'augmentation de l'émissivité lors de la formation de la glace.",
            font_size=30
        )
        conclusion.to_edge(DOWN)
        
        self.play(Write(conclusion))
        self.wait(2)