import discord
import asyncio

class Vote():
  def __init__(
    self, goal: int, objective: str, client, author, channel):
    
    self.goal = goal
    self.objective = objective
    self.client = client
    self.author = author
    self.voters = [author]
    self.total = 1
    self.channel = channel

  async def voting(self):
    print('Iniciou')    
    await self.client.send_message(self.channel, f'Votação {self.objective} iniciada. {self.total}/{self.goal}')
    await self.client.send_message(self.channel, 'Utilize !up para votar')
    while True:
      print('Aguardando mensagem')
      vote = await self.client.wait_for_message(timeout=60.0, content='!up', channel=self.channel)
      if not vote:
        msg = f"\
        Votação encerrada !\n{self.objective} - {self.total}/{self.goal}"
        return False
      if vote.author not in self.voters:
        self.total += 1
        self.voters.append(vote.author)
        if self.total >= self.goal:
          msg = f"\
          Votação encerrada !\n{self.objective} - {self.total}/{self.goal}"
          await self.client.send_message(vote.channel, msg)
          return True
        print(self.total, self.goal)
        msg = f"""
        {vote.author} Votou !\n{self.objective} - {self.total}/{self.goal}

        digite !up para votar
        """
        await self.client.send_message(vote.channel, msg)
