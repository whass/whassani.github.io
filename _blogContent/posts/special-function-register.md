title: Special Function Register
date: 2015-02-17
categories:
- Embedded

A Special Function Register (ou Special Purpose Register, ou simplement registre spécial) est un registre dans un microprocesseur, qui contrôle ou surveille les différents aspects des fonctions du microprocesseur. En fonction de l'architecture du processeur, ceci peut inclure, mais ne sont pas limités à:



	
  * I/O et le contrôle périphérique (tels que les ports série ou à usage général OI)

	
  * Timers (minuteries)

	
  * Stack pointer (pointeur de pile)

	
  * stack limit (limite de pile) (pour éviter les débordements)

	
  * PC Program counter (compteur de programme)

	
  * subroutine return address (adresse de retour sous-programme)

	
  * état du processeur (l'entretien d'une interruption, le fonctionnement en mode protégé, etc.)

	
  * code condition (codes conditionnelle, l'instruction if par ex.) (résultat de comparaisons précédentes)


Du fait que les registres spéciaux sont étroitement liées à certaines fonctions spéciales ou le statut du processeur, ils pourraient ne pas être directement accessible en écriture par instructions normales (telles que les ajouts, déplacements, etc.). Au lieu de cela, certains registres spéciaux dans certaines architectures de processeurs nécessitent des instructions spéciales pour les modifier. Par **exemple**, le compteur de programme ne est pas directement accessible en écriture dans de nombreuses architectures de processeur. Au lieu de cela, le programmeur utilise des instructions telles que le **retour du sous-programme**, **saut**, ou une **branch** pour modifier le compteur de programme. Un autre exemple, le registre de "**code condition**" peut ne pas directement accessible en écriture, et ne peut être modifié que par que per une instruction de comparaison.
