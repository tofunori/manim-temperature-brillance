from manim import *
import numpy as np

class MicrowaveRemoteSensing(Scene):
    def construct(self):
        # Couleurs personnalisées pour rendre l'animation plus professionnelle
        WATER_COLOR = "#0C2D48"
        ICE_COLOR = "#B3E5FC"
        SATELLITE_COLOR = "#78909C"
        WAVE_COLOR = "#FFD700"
        
        # Titre principal avec animation plus sophistiquée
        title = Text("Télédétection Micro-onde en Arctique", font_size=48)
        subtitle = Text("Principes physiques et applications", font_size=32, color=BLUE_C)
        subtitle.next_to(title, DOWN)
        
        title_group = VGroup(title, subtitle)
        
        self.play(
            Write(title, run_time=1.5),
            FadeIn(subtitle, shift=UP*0.5, run_time=1.5)
        )
        self.wait(1)
        self.play(
            title_group.animate.scale(0.6).to_edge(UP),
            run_time=1
        )
        
        # Introduction au concept de température de brillance
        tb_def = Text("Température de Brillance (Tᴮ)", font_size=36, color=YELLOW_C)
        tb_def.next_to(title_group, DOWN, buff=0.5)
        
        tb_equation = MathTex(
            "T_B(\\theta, \\nu) = ", "\\varepsilon(\\theta, \\nu)", "\\cdot T_{physique}",
            font_size=36
        )
        tb_equation.next_to(tb_def, DOWN, buff=0.3)
        
        tb_explanation = BulletedList(
            "Température apparente perçue par un capteur satellite",
            "Dépend de l'émissivité de la surface",
            "Varie selon l'angle (θ) et la fréquence (ν)",
            font_size=28
        )
        tb_explanation.next_to(tb_equation, DOWN, buff=0.3)
        
        self.play(Write(tb_def))
        self.wait(0.5)
        self.play(Write(tb_equation))
        self.wait(0.5)
        self.play(Write(tb_explanation), run_time=2)
        self.wait(2)
        
        # Effacer pour la prochaine section
        self.play(
            FadeOut(tb_def),
            FadeOut(tb_equation),
            FadeOut(tb_explanation),
            run_time=1
        )
        
        # Expliquer le concept d'émissivité
        emissivity_title = Text("Émissivité (ε)", font_size=36, color=GREEN_C)
        emissivity_title.next_to(title_group, DOWN, buff=0.5)
        
        emissivity_def = BulletedList(
            "Mesure de la capacité d'un matériau à émettre de l'énergie",
            "Varie entre 0 (réflecteur parfait) et 1 (corps noir)",
            font_size=28
        )
        emissivity_def.next_to(emissivity_title, DOWN, buff=0.3)
        
        # Tableau des valeurs d'émissivité
        emissivity_table = Table(
            [["Eau de mer", "0.45-0.65"],
             ["Glace de mer récente", "0.92"],
             ["Glace de mer pluriannuelle", "0.84-0.90"],
             ["Neige sèche", "0.65-0.83"]],
            col_labels=["Surface", "Émissivité (19-37 GHz)"],
            include_outer_lines=True
        )
        emissivity_table.scale(0.6)
        emissivity_table.next_to(emissivity_def, DOWN, buff=0.3)
        
        self.play(Write(emissivity_title))
        self.play(Write(emissivity_def), run_time=1.5)
        self.play(Create(emissivity_table), run_time=2)
        self.wait(2)
        
        # Effacer pour la prochaine section
        self.play(
            FadeOut(emissivity_title),
            FadeOut(emissivity_def),
            FadeOut(emissivity_table),
            run_time=1
        )
        
        # Simulation du satellite, de la surface d'eau et de la glace
        satellite = SVGMobject("satellite").set_color(SATELLITE_COLOR)
        satellite.scale(0.5).to_edge(UP + RIGHT, buff=1)
        
        ocean = Rectangle(width=10, height=1.5, fill_opacity=0.8, fill_color=WATER_COLOR, stroke_color=WHITE)
        ocean.to_edge(DOWN, buff=1)
        
        ocean_label = Text("Océan Arctique", font_size=24, color=WHITE)
        ocean_label.next_to(ocean, UP, buff=0.2)
        
        # Créer les axes pour les graphiques
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.5, 0.5],
            axis_config={"include_tip": False, "include_numbers": True},
            x_length=6,
            y_length=3,
        )
        axes.to_edge(LEFT, buff=1)
        axes.shift(UP*0.5)
        
        x_label = axes.get_x_axis_label("Temps (jours)", edge=DOWN, direction=DOWN)
        y_label = axes.get_y_axis_label("Valeur normalisée")
        
        # Définir les fonctions pour les courbes
        def emissivity_function(x):
            if x < 3:
                return 0.55  # Émissivité de l'eau
            elif x < 6:
                return 0.55 + (0.92 - 0.55) * (x - 3) / 3  # Transition
            else:
                return 0.92  # Émissivité de la glace
        
        def temp_physical(x):
            # Température physique qui diminue légèrement pendant le gel
            if x < 3:
                return 1  # Température initiale
            elif x < 6:
                return 1 - 0.2 * (x - 3) / 3  # Diminution pendant la transition
            else:
                return 0.8  # Température stabilisée
        
        def temp_brightness(x):
            # Température de brillance = émissivité * température physique
            return emissivity_function(x) * temp_physical(x)
        
        # Tracer les courbes
        emissivity_curve = axes.plot(emissivity_function, x_range=[0, 10], color=GREEN)
        temp_phys_curve = axes.plot(temp_physical, x_range=[0, 10], color=BLUE)
        tb_curve = axes.plot(temp_brightness, x_range=[0, 10], color=RED)
        
        # Étiquettes pour les courbes
        emissivity_label = Text("Émissivité (ε)", font_size=20, color=GREEN).next_to(axes, RIGHT, buff=0.2)
        emissivity_label.shift(UP*1)
        
        temp_phys_label = Text("Température physique", font_size=20, color=BLUE).next_to(axes, RIGHT, buff=0.2)
        temp_phys_label.shift(UP*0.5)
        
        tb_label = Text("Température de brillance (Tᴮ)", font_size=20, color=RED).next_to(axes, RIGHT, buff=0.2)
        tb_label.shift(UP*0)
        
        # Animer l'apparition du système physique
        self.play(
            Create(satellite),
            Create(ocean),
            Write(ocean_label),
            run_time=1.5
        )
        
        # Animer l'apparition des axes et des courbes
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            run_time=1.5
        )
        
        # Animation des courbes
        self.play(Create(temp_phys_curve), Write(temp_phys_label), run_time=1.5)
        self.wait(0.5)
        
        self.play(Create(emissivity_curve), Write(emissivity_label), run_time=1.5)
        self.wait(0.5)
        
        self.play(Create(tb_curve), Write(tb_label), run_time=1.5)
        self.wait(1)
        
        # Animation des micro-ondes
        def create_microwave(start, end, num_waves=4):
            path = Line(start, end)
            waves = []
            for i in range(num_waves):
                t = i / (num_waves - 1) if num_waves > 1 else 0.5
                point = path.point_from_proportion(t)
                wave = Circle(radius=0.1, color=WAVE_COLOR, fill_opacity=0, stroke_width=2)
                wave.move_to(point)
                waves.append(wave)
            return VGroup(*waves)
        
        def animate_microwave_propagation(waves, direction, run_time=1.5):
            animations = []
            for wave in waves:
                animations.append(
                    wave.animate.scale(3).set_opacity(0).shift(direction)
                )
            self.play(*animations, run_time=run_time)
        
        # Point de départ des micro-ondes (surface)
        surface_point = ocean.get_top() + UP*0.2
        
        # Créer et animer les micro-ondes à différents moments
        # 1. Eau de mer (émissivité faible)
        microwaves_water = create_microwave(surface_point, satellite.get_center())
        self.play(FadeIn(microwaves_water))
        animate_microwave_propagation(microwaves_water, UP*2)
        
        # Animation du gel progressif
        ice_formation = Rectangle(
            width=0, height=1.5, 
            fill_opacity=0.8, 
            fill_color=ICE_COLOR,
            stroke_width=0
        )
        ice_formation.align_to(ocean, DOWN+LEFT)
        
        self.play(
            GrowFromPoint(ice_formation, ice_formation.get_center(), rate_func=linear),
            ice_formation.animate.stretch_to_fit_width(10),
            run_time=5
        )
        
        # 2. Glace de mer (émissivité élevée)
        microwaves_ice = create_microwave(surface_point, satellite.get_center(), num_waves=8)
        self.play(FadeIn(microwaves_ice))
        animate_microwave_propagation(microwaves_ice, UP*2)
        
        # Annotations sur le graphique pour expliquer le phénomène
        explanation_box = VGroup(
            Text("Phénomène observé :", font_size=28, color=YELLOW_C),
            BulletedList(
                "Émissivité de l'eau faible (0.45-0.65)",
                "Émissivité de la glace élevée (≈ 0.92)",
                "Tb augmente malgré une température physique constante/diminuant",
                font_size=24
            )
        ).arrange(DOWN, aligned_edge=LEFT)
        
        explanation_box.next_to(axes, DOWN, buff=0.5)
        
        self.play(Write(explanation_box), run_time=2)
        self.wait(1)
        
        # Applications pratiques
        applications_title = Text("Applications en télédétection", font_size=32, color=YELLOW_C)
        applications_title.to_edge(RIGHT).shift(UP*0.5)
        
        applications = BulletedList(
            "Suivi de l'étendue des glaces de mer",
            "Détection des polynies et chenaux",
            "Mesure des taux de fonte/gel",
            "Estimation de l'épaisseur de la glace",
            "Cartographie des types de glace",
            font_size=24
        )
        applications.next_to(applications_title, DOWN, aligned_edge=LEFT)
        
        self.play(
            Write(applications_title),
            run_time=1
        )
        self.play(
            Write(applications),
            run_time=2
        )
        self.wait(1)
        
        # Fréquences utilisées en télédétection micro-onde
        frequencies_title = Text("Fréquences courantes", font_size=28, color=YELLOW_C)
        frequencies_title.next_to(applications, DOWN, buff=0.5)
        
        frequencies = BulletedList(
            "6.9 GHz (λ ≈ 4.3 cm)",
            "18.7 GHz (λ ≈ 1.6 cm)",
            "23.8 GHz (λ ≈ 1.3 cm)",
            "36.5 GHz (λ ≈ 8.2 mm)",
            "89.0 GHz (λ ≈ 3.4 mm)",
            font_size=20
        )
        frequencies.next_to(frequencies_title, DOWN, aligned_edge=LEFT)
        
        self.play(
            Write(frequencies_title),
            run_time=1
        )
        self.play(
            Write(frequencies),
            run_time=2
        )
        self.wait(2)
        
        # Conclusion finale
        conclusion = Text(
            "La télédétection micro-onde permet de surveiller les changements\n"
            "des surfaces glacées en Arctique même par temps nuageux ou la nuit.",
            font_size=30,
            t2c={"télédétection micro-onde": YELLOW_C, "Arctique": BLUE_C}
        )
        conclusion.to_edge(DOWN, buff=0.2)
        
        self.play(
            FadeOut(explanation_box),
            Write(conclusion),
            run_time=2
        )
        self.wait(3)


class BrightnessTemperatureEvolution(Scene):
    def construct(self):
        # Titre en français avec style amélioré
        title = Tex(r"\textbf{Évolution de la Température de Brillance}", font_size=48)
        subtitle = Tex(r"\textit{Pendant le gel de l'eau salée en Arctique}", font_size=36, color=BLUE)
        
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        
        self.play(Write(title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP*0.2), run_time=1)
        self.wait(1)
        
        self.play(
            title_group.animate.scale(0.7).to_edge(UP, buff=0.5),
            run_time=1
        )
        
        # Configuration des axes avec style amélioré
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.2, 0.2],
            axis_config={
                "include_tip": True,
                "include_numbers": True,
                "font_size": 24,
            },
            x_length=9,
            y_length=5,
        ).shift(DOWN*0.5)
        
        x_label = axes.get_x_axis_label(Tex("Temps (jours)"), edge=DOWN, direction=DOWN)
        y_label = axes.get_y_axis_label(Tex("Valeur normalisée"), edge=LEFT, direction=LEFT)
        
        axes_labels = VGroup(x_label, y_label)
        
        # Définition scientifique des fonctions pour les courbes
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
        
        # Création des courbes avec style amélioré
        temp_phys_curve = axes.plot(
            physical_temperature,
            x_range=[0, 10],
            color=BLUE,
            stroke_width=3,
        )
        
        emissivity_curve = axes.plot(
            emissivity,
            x_range=[0, 10],
            color=GREEN,
            stroke_width=3,
        )
        
        tb_curve = axes.plot(
            brightness_temperature,
            x_range=[0, 10],
            color=RED,
            stroke_width=4,
        )
        
        # Étiquettes des courbes avec style amélioré
        temp_phys_label = Tex(r"Température physique", color=BLUE, font_size=28)
        temp_phys_label.next_to(temp_phys_curve.get_end(), RIGHT)
        
        emissivity_label = Tex(r"Émissivité ($\varepsilon$)", color=GREEN, font_size=28)
        emissivity_label.next_to(emissivity_curve.get_end(), RIGHT)
        
        tb_label = Tex(r"Température de brillance ($T_B$)", color=RED, font_size=28)
        tb_label.next_to(tb_curve.get_end(), RIGHT)
        
        curve_labels = VGroup(temp_phys_label, emissivity_label, tb_label)
        
        # Animation progressive
        self.play(Create(axes), Write(axes_labels), run_time=1.5)
        self.wait(0.5)
        
        # Visualisation de l'océan et de la formation de glace
        ocean = Rectangle(width=9, height=2, fill_opacity=0.8, fill_color="#0C2D48", stroke_color=BLUE_E)
        ocean.next_to(axes, DOWN, buff=0.75)
        
        ocean_label = Tex(r"Océan Arctique", font_size=30, color=BLUE_E)
        ocean_label.next_to(ocean, UP, buff=0.2)
        
        self.play(
            FadeIn(ocean),
            Write(ocean_label),
            run_time=1
        )
        
        # Textes d'explication scientifique
        phase_water = Tex(r"Phase liquide: émissivité basse", font_size=24, color=WHITE)
        phase_water.next_to(ocean, DOWN, buff=0.2).align_to(ocean, LEFT).shift(RIGHT*1.5)
        
        phase_transition = Tex(r"Transition: formation de cristaux de glace", font_size=24, color=WHITE)
        phase_transition.move_to(phase_water.get_center() + RIGHT*3)
        
        phase_ice = Tex(r"Phase solide: émissivité élevée", font_size=24, color=WHITE)
        phase_ice.move_to(phase_water.get_center() + RIGHT*6)
        
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
        
        # Visualisation de la formation de glace
        ice_formation = Rectangle(width=0, height=2, fill_opacity=0.9, fill_color="#B3E5FC", stroke_width=0)
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
        
        # Ajout des formules scientifiques
        formula_box = Rectangle(width=5, height=2.8, fill_opacity=0.8, fill_color=BLACK, stroke_color=YELLOW)
        formula_box.to_edge(LEFT, buff=0.5).shift(UP*0.5)
        
        formula_title = Tex(r"\textbf{Équations fondamentales}", font_size=30, color=YELLOW)
        formula_title.next_to(formula_box.get_top(), DOWN, buff=0.2)
        
        tb_formula = MathTex(
            r"T_B(\theta, \nu) = \varepsilon(\theta, \nu) \cdot T_{phys}",
            font_size=28
        )
        tb_formula.next_to(formula_title, DOWN, buff=0.3)
        
        formula_explanation1 = Tex(r"$T_B$ : Température de brillance", font_size=22)
        formula_explanation2 = Tex(r"$\varepsilon$ : Émissivité (dépend de $\theta$, $\nu$)", font_size=22)
        formula_explanation3 = Tex(r"$T_{phys}$ : Température physique", font_size=22)
        
        explanations = VGroup(formula_explanation1, formula_explanation2, formula_explanation3)
        explanations.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        explanations.next_to(tb_formula, DOWN, buff=0.3)
        
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
        
        # Conclusion scientifique
        conclusion_box = Rectangle(width=5, height=2.5, fill_opacity=0.8, fill_color=BLACK, stroke_color=BLUE)
        conclusion_box.to_edge(RIGHT, buff=0.5).shift(UP*0.5)
        
        conclusion_title = Tex(r"\textbf{Implications scientifiques}", font_size=30, color=BLUE)
        conclusion_title.next_to(conclusion_box.get_top(), DOWN, buff=0.2)
        
        conclusion_points = BulletedList(
            "Détection des transitions de phase",
            "Cartographie de la glace de mer",
            "Suivi des cycles de gel/dégel",
            "Étude des propriétés de la glace",
            font_size=22
        )
        conclusion_points.next_to(conclusion_title, DOWN, buff=0.2)
        
        self.play(
            FadeIn(conclusion_box),
            Write(conclusion_title),
            run_time=1
        )
        
        self.play(
            Write(conclusion_points),
            run_time=2
        )
        self.wait(1)
        
        # Message final
        final_message = Tex(
            r"\textbf{La température de brillance augmente significativement}\\",
            r"\textbf{malgré une température physique constante ou en légère baisse,}\\",
            r"\textbf{en raison de l'augmentation de l'émissivité lors de la formation de glace.}",
            font_size=32
        )
        final_message.to_edge(DOWN, buff=0.5)
        
        self.play(
            Write(final_message),
            run_time=2
        )
        self.wait(3)


class SatelliteMicroResonaTechnology(Scene):
    def construct(self):
        # Titre avec animation élégante
        title = Text("Télédétection Micro-onde par Satellite", font_size=48)
        subtitle = Text("Technologie & Instrumentation", font_size=36, color=BLUE)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(1)
        
        self.play(
            VGroup(title, subtitle).animate.scale(0.6).to_edge(UP, buff=0.5),
            run_time=1
        )
        
        # Présentation des capteurs satellites
        sensors_title = Text("Capteurs Satellites Principaux", font_size=36, color=YELLOW)
        sensors_title.next_to(subtitle, DOWN, buff=0.7)
        
        sensors_table = Table(
            [["SMMR", "1978-1987", "6.6-37 GHz", "Nimbus-7"],
             ["SSM/I", "1987-2009", "19-85.5 GHz", "DMSP F8-F15"],
             ["AMSR-E", "2002-2011", "6.9-89 GHz", "Aqua"],
             ["AMSR2", "2012-", "6.9-89 GHz", "GCOM-W1"],
             ["SMOS", "2009-", "1.4 GHz (L-band)", "SMOS"]],
            col_labels=["Capteur", "Période", "Fréquences", "Plateforme"],
            include_outer_lines=True,
            line_config={"stroke_width": 2}
        )
        sensors_table.scale(0.7)
        sensors_table.next_to(sensors_title, DOWN, buff=0.5)
        
        self.play(Write(sensors_title), run_time=1)
        self.play(Create(sensors_table), run_time=2)
        self.wait(1.5)
        
        # Schéma de l'orbite polaire
        orbit_title = Text("Orbite Polaire Héliosynchrone", font_size=30, color=GREEN)
        orbit_title.to_edge(LEFT, buff=1).shift(DOWN * 2)
        
        earth = Circle(radius=1.2, color=BLUE)
        earth.next_to(orbit_title, DOWN, buff=0.5)
        earth.shift(RIGHT * 1.5)
        
        # Dessiner l'orbite polaire
        orbit = Ellipse(width=3, height=3.2, color=WHITE)
        orbit.move_to(earth.get_center())
        
        # Satellite en mouvement
        satellite = Triangle(color=RED, fill_opacity=1).scale(0.2)
        
        # Animation de l'orbite polaire
        self.play(Write(orbit_title), Create(earth), run_time=1.5)
        self.play(Create(orbit), run_time=1)
        
        # Animation du satellite sur son orbite
        satellite_path = ParametricFunction(
            lambda t: earth.get_center() + np.array([
                1.5 * np.cos(t),
                1.6 * np.sin(t),
                0
            ]),
            t_range=[0, 2*PI],
            color=RED
        )
        
        satellite.move_to(satellite_path.point_from_proportion(0))
        self.add(satellite)
        
        self.play(
            MoveAlongPath(satellite, satellite_path),
            run_time=5,
            rate_func=linear
        )
        self.wait(1)
        
        # Explication du principe de fonctionnement des radiomètres
        principle_title = Text("Principe du Radiomètre Micro-onde", font_size=30, color=YELLOW)
        principle_title.to_edge(RIGHT, buff=1).shift(DOWN * 2)
        
        principle_points = BulletedList(
            "Mesure passive du rayonnement émis",
            "Détection de la température de brillance",
            "Multiple fréquences et polarisations",
            "Calcul de l'émissivité des surfaces",
            font_size=22
        )
        principle_points.next_to(principle_title, DOWN, buff=0.3)
        
        self.play(Write(principle_title), run_time=1)
        self.play(Write(principle_points), run_time=2)
        self.wait(1.5)
        
        # Avantages et applications
        self.play(
            FadeOut(sensors_title),
            FadeOut(sensors_table),
            FadeOut(orbit_title),
            FadeOut(earth),
            FadeOut(orbit),
            FadeOut(satellite),
            FadeOut(principle_title),
            FadeOut(principle_points),
            run_time=1
        )
        
        advantages_title = Text("Avantages de la Télédétection Micro-onde", font_size=36, color=GREEN)
        advantages_title.next_to(subtitle, DOWN, buff=0.7)
        
        advantages = VGroup(
            BulletedList(
                "Fonctionnement jour et nuit",
                "Pénétration des nuages",
                "Sensibilité aux propriétés diélectriques",
                "Mesure de l'épaisseur de glace",
                font_size=28
            ),
            BulletedList(
                "Suivi des changements saisonniers",
                "Cartographie à l'échelle globale",
                "Séries temporelles de 40+ ans",
                "Mesures multi-fréquences",
                font_size=28
            )
        ).arrange(RIGHT, buff=1)
        
        advantages.next_to(advantages_title, DOWN, buff=0.5)
        
        self.play(Write(advantages_title), run_time=1)
        self.play(Write(advantages), run_time=2.5)
        self.wait(1.5)
        
        # Algorithmes et produits dérivés
        algorithms_title = Text("Algorithmes & Produits", font_size=36, color=BLUE)
        algorithms_title.next_to(advantages, DOWN, buff=0.7)
        
        algorithms = BulletedList(
            "NASA Team Algorithm",
            "Bootstrap Algorithm",
            "ASI Algorithm (AMSR-E/AMSR2)",
            "Cartes de concentration de glace",
            "Indice d'âge de la glace",
            "Détection du dégel de surface",
            font_size=28
        )
        algorithms.next_to(algorithms_title, DOWN, buff=0.3)
        
        self.play(Write(algorithms_title), run_time=1)
        self.play(Write(algorithms), run_time=2)
        self.wait(1.5)
        
        # Conclusion
        self.play(
            FadeOut(advantages_title),
            FadeOut(advantages),
            FadeOut(algorithms_title),
            FadeOut(algorithms),
            run_time=1
        )
        
        conclusion = Text(
            "La télédétection micro-onde constitue un outil essentiel\n"
            "pour surveiller et comprendre les changements climatiques\n"
            "dans les régions polaires.",
            font_size=36,
            t2c={"télédétection micro-onde": YELLOW, "changements climatiques": RED}
        )
        conclusion.next_to(subtitle, DOWN, buff=1.5)
        
        self.play(Write(conclusion), run_time=2)
        self.wait(2)