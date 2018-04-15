public class Wand{
	protected final int range;
	protected int effect;
	protected Player owner;
	public Wand(int range, int damage, Player owner){
		this.range = range;
		this.effect = damage;
		this.owner = owner;
	}

	public void enhance() {
		this.effect += 5;
	}

	public void action(int posx, int posy){
		System.out.println("You are using wand healing " + posx + " " + posy + ".");

		if (this.owner.pos.distance(posx, posy)  <= this.range) {
			// search for all targets with target coordinates.
			Player player = owner.game.getPlayer(posx, posy);

			if(player != null ) 
			{
				if ((this.owner).race != player.race){
					System.out.println("You are the different race, cannot do that.");
				}
				else{
					player.increaseHealth(this.effect);
				}
			}
		} else {
			System.out.println("Out of reach.");
		}
	}

	public int getEffect() {
		return this.effect;
	}

	public int getRange() {
		return this.range;
	}
}