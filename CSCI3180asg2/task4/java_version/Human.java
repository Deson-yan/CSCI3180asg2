public class Human extends Player {
	
	public Human(int posx, int posy, int index, SurvivalGame game, boolean isHealer) {
		super(80, 2, posx, posy, index, game, isHealer);
		
		this.myString = 'H' + Integer.toString(index);
		if (isHealer){
			this.equipment = new Wand(5,10,this);
		}
		else{
			this.equipment = new Rifle(this);
		}
		this.race = "H";
	}

	public void teleport() {
		super.teleport();
		if (this.isHealer){
			((Wand)this.equipment).enhance();
		}
		else{
			((Rifle)this.equipment).enhance();
		}
	}
	
	public void distance(int posx, int posy)
	{
		
	}
	
	@Override
	public void askForMove() {
		// TODO Auto-generated method stub
		if (isHealer){
			System.out.println(String.format("You are a human (H%d) using Wand. (Range: %d, Effect: %d)",this.index,
				this.equipment.getRange(), this.equipment.getEffect()));
		}
		else{
			System.out.println(String.format("You are a human (H%d) using Rifle. (Range %d, Ammo #: %d, Damage per shot: %d)", this.index, 
				this.equipment.getRange(),((Rifle)this.equipment).getAmmo(),
				this.equipment.getEffect() ));
		}

		super.askForMove();
		
	}

}
