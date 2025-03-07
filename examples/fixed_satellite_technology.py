from manim import *

class SatelliteMicroReSonaFixed(Scene):
    """
    Version corrigée de la classe SatelliteMicroResonaTechnology
    avec correction des erreurs de Table et optimisation pour MiKTeX
    """
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
        
        # Présentation des capteurs satellites - sans utiliser Table
        sensors_title = Text("Capteurs Satellites Principaux", font_size=36, color=YELLOW)
        sensors_title.next_to(subtitle, DOWN, buff=0.7)
        
        # Créer un tableau manuellement avec des Textes et des rectangles
        # C'est plus stable que d'utiliser la classe Table qui a causé des erreurs
        table_data = [
            ["Capteur", "Période", "Fréquences", "Plateforme"],
            ["SMMR", "1978-1987", "6.6-37 GHz", "Nimbus-7"],
            ["SSM/I", "1987-2009", "19-85.5 GHz", "DMSP F8-F15"],
            ["AMSR-E", "2002-2011", "6.9-89 GHz", "Aqua"],
            ["AMSR2", "2012-", "6.9-89 GHz", "GCOM-W1"],
            ["SMOS", "2009-", "1.4 GHz (L-band)", "SMOS"]
        ]
        
        # Créer la grille du tableau
        table_group = VGroup()
        cell_width = 2.2
        cell_height = 0.5
        rows = len(table_data)
        cols = len(table_data[0])
        
        for i in range(rows):
            for j in range(cols):
                # Créer le rectangle de la cellule
                cell = Rectangle(
                    width=cell_width, 
                    height=cell_height,
                    stroke_width=2,
                    fill_opacity=0.1 if i == 0 else 0
                )
                cell.move_to(RIGHT * (j * cell_width - (cols-1) * cell_width / 2) + 
                             DOWN * (i * cell_height - (rows-1) * cell_height / 2))
                
                # Créer le texte de la cellule
                text = Text(table_data[i][j], font_size=18)
                text.move_to(cell.get_center())
                
                # Ajouter la cellule et le texte au groupe
                table_group.add(cell, text)
        
        # Positionner le tableau
        table_group.scale(0.8)
        table_group.next_to(sensors_title, DOWN, buff=0.5)
        
        # Animation de l'affichage du tableau
        self.play(Write(sensors_title), run_time=1)
        self.play(Create(table_group), run_time=2)
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
        
        # Utilisation de Text au lieu de BulletedList pour éviter les problèmes LaTeX
        principle_item1 = Text("• Mesure passive du rayonnement émis", font_size=22)
        principle_item2 = Text("• Détection de la température de brillance", font_size=22)
        principle_item3 = Text("• Multiple fréquences et polarisations", font_size=22)
        principle_item4 = Text("• Calcul de l'émissivité des surfaces", font_size=22)
        
        principle_points = VGroup(principle_item1, principle_item2, principle_item3, principle_item4)
        principle_points.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        principle_points.next_to(principle_title, DOWN, buff=0.3)
        
        self.play(Write(principle_title), run_time=1)
        self.play(Write(principle_points), run_time=2)
        self.wait(1.5)
        
        # Avantages et applications
        self.play(
            FadeOut(sensors_title),
            FadeOut(table_group),
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
        
        # Créer des listes à puces sans utiliser BulletedList
        adv_left_items = [
            "• Fonctionnement jour et nuit",
            "• Pénétration des nuages",
            "• Sensibilité aux propriétés diélectriques",
            "• Mesure de l'épaisseur de glace",
        ]
        
        adv_right_items = [
            "• Suivi des changements saisonniers",
            "• Cartographie à l'échelle globale",
            "• Séries temporelles de 40+ ans",
            "• Mesures multi-fréquences",
        ]
        
        adv_left = VGroup(*[Text(text, font_size=28) for text in adv_left_items])
        adv_left.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        adv_right = VGroup(*[Text(text, font_size=28) for text in adv_right_items])
        adv_right.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        advantages = VGroup(adv_left, adv_right).arrange(RIGHT, buff=1)
        advantages.next_to(advantages_title, DOWN, buff=0.5)
        
        self.play(Write(advantages_title), run_time=1)
        self.play(Write(advantages), run_time=2.5)
        self.wait(1.5)
        
        # Algorithmes et produits dérivés
        algorithms_title = Text("Algorithmes & Produits", font_size=36, color=BLUE)
        algorithms_title.next_to(advantages, DOWN, buff=0.7)
        
        algorithms_items = [
            "• NASA Team Algorithm",
            "• Bootstrap Algorithm",
            "• ASI Algorithm (AMSR-E/AMSR2)",
            "• Cartes de concentration de glace",
            "• Indice d'âge de la glace",
            "• Détection du dégel de surface",
        ]
        
        algorithms = VGroup(*[Text(text, font_size=28) for text in algorithms_items])
        algorithms.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
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


class ImprovedMicrowaveRemoteSensing(Scene):
    """
    Version optimisée de la classe MicrowaveRemoteSensing
    avec correction des problèmes de LaTeX
    """
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
        
        # Utiliser Text au lieu de MathTex pour éviter les problèmes LaTeX
        tb_equation = Text("Tᴮ(θ, ν) = ε(θ, ν) · Tphysique", font_size=36)
        tb_equation.next_to(tb_def, DOWN, buff=0.3)
        
        # Utiliser des textes individuels au lieu de BulletedList
        tb_explanation1 = Text("• Température apparente perçue par un capteur satellite", font_size=28)
        tb_explanation2 = Text("• Dépend de l'émissivité de la surface", font_size=28)
        tb_explanation3 = Text("• Varie selon l'angle (θ) et la fréquence (ν)", font_size=28)
        
        tb_explanation = VGroup(tb_explanation1, tb_explanation2, tb_explanation3)
        tb_explanation.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
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
        
        # Utiliser des textes individuels au lieu de BulletedList
        emissivity_def1 = Text("• Mesure de la capacité d'un matériau à émettre de l'énergie", font_size=28)
        emissivity_def2 = Text("• Varie entre 0 (réflecteur parfait) et 1 (corps noir)", font_size=28)
        
        emissivity_def = VGroup(emissivity_def1, emissivity_def2)
        emissivity_def.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        emissivity_def.next_to(emissivity_title, DOWN, buff=0.3)
        
        # Tableau des valeurs d'émissivité créé manuellement
        table_title = Text("Valeurs d'émissivité typiques:", font_size=28)
        table_title.next_to(emissivity_def, DOWN, buff=0.4)
        
        table_data = [
            ["Surface", "Émissivité (19-37 GHz)"],
            ["Eau de mer", "0.45-0.65"],
            ["Glace de mer récente", "0.92"],
            ["Glace de mer pluriannuelle", "0.84-0.90"],
            ["Neige sèche", "0.65-0.83"]
        ]
        
        # Créer le tableau manuellement
        table_group = VGroup()
        cell_width = 3.0
        cell_height = 0.5
        rows = len(table_data)
        cols = len(table_data[0])
        
        for i in range(rows):
            for j in range(cols):
                cell = Rectangle(
                    width=cell_width, 
                    height=cell_height,
                    stroke_width=2,
                    fill_opacity=0.1 if i == 0 else 0
                )
                cell.move_to(RIGHT * (j * cell_width - (cols-1) * cell_width / 2) + 
                             DOWN * (i * cell_height - (rows-1) * cell_height / 2 + 4))
                
                text = Text(table_data[i][j], font_size=20)
                text.move_to(cell.get_center())
                
                table_group.add(cell, text)
        
        self.play(Write(emissivity_title))
        self.play(Write(emissivity_def), run_time=1.5)
        self.play(Write(table_title), run_time=1)
        self.play(Create(table_group), run_time=2)
        self.wait(2)
        
        # Effacer pour la prochaine section
        self.play(
            FadeOut(emissivity_title),
            FadeOut(emissivity_def),
            FadeOut(table_title),
            FadeOut(table_group),
            run_time=1
        )
        
        # Simulation du satellite, de la surface d'eau et de la glace
        satellite = Triangle(fill_opacity=1, color=SATELLITE_COLOR)
        satellite.scale(0.3).to_edge(UP + RIGHT, buff=1)
        
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
        
        x_label = Text("Temps (jours)", font_size=20)
        x_label.next_to(axes, DOWN, buff=0.2)
        
        y_label = Text("Valeur normalisée", font_size=20)
        y_label.next_to(axes, LEFT, buff=0.2)
        y_label.rotate(PI/2)
        
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
        
        # Annotations sur le graphique pour expliquer le phénomène - utilisez Text
        explanation_box = Rectangle(width=6, height=2, fill_opacity=0.7, fill_color=BLACK, stroke_color=YELLOW, stroke_width=2)
        explanation_box.to_corner(DOWN + RIGHT, buff=0.5)
        
        explanation_title = Text("Phénomène observé :", font_size=28, color=YELLOW_C)
        explanation_title.next_to(explanation_box, UP, buff=0.2)
        
        explanation_text1 = Text("• Émissivité de l'eau faible (0.45-0.65)", font_size=24)
        explanation_text2 = Text("• Émissivité de la glace élevée (≈ 0.92)", font_size=24)
        explanation_text3 = Text("• Tᴮ augmente malgré une température physique constante/diminuant", font_size=24)
        
        explanation_text = VGroup(explanation_text1, explanation_text2, explanation_text3)
        explanation_text.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explanation_text.move_to(explanation_box.get_center())
        
        self.play(
            Create(explanation_box),
            Write(explanation_title),
            run_time=1.5
        )
        
        self.play(
            Write(explanation_text),
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
            FadeOut(explanation_title),
            FadeOut(explanation_text),
            Write(conclusion),
            run_time=2
        )
        self.wait(3)
